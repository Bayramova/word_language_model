import click
import torch

import text_generator.data as data


@click.command()
@click.option(
    "--input-dir",
    type=click.Path(exists=True, dir_okay=False),
    default="data/data.txt",
    show_default=True,
    help="Path to file with training data.",
)
@click.option(
    "--checkpoint",
    type=click.Path(exists=True, dir_okay=False),
    default="model.pt",
    show_default=True,
    help="Path to the trained model.",
)
@click.option("--prefix", type=str, default=None, show_default=True, help="Seed text.")
@click.option(
    "--length",
    type=int,
    default="10",
    show_default=True,
    help="Number of words to generate.",
)
def generate(input_dir, checkpoint, prefix, length):
    """This script generates new sentences sampled from the language model."""

    # Load the model
    model = torch.load(checkpoint)

    # Load data
    corpus = data.Corpus(input_dir)
    ntoken = len(corpus.dictionary)

    if prefix is None or prefix not in corpus.dictionary.word2idx:
        # Choose random word from dictionary
        input = torch.randint(ntoken, (1, 1), dtype=torch.int64)
        click.echo(f"Random prefix: {corpus.dictionary.idx2word[input]}")
    else:
        input = torch.tensor(corpus.dictionary.word2idx[prefix]).reshape((1, 1))

    quote = [corpus.dictionary.idx2word[input]]
    for _ in range(length):
        output = model(input)
        word_idx = torch.multinomial(output, 1)
        input.fill_(word_idx[0][0])

        word = corpus.dictionary.idx2word[word_idx]
        quote.append(word)

    click.echo(f'Generated sequence:\n{" ".join(quote)}')