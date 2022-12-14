# Word-level Language Modeling
This project trains a multi-layer LSTM model with pre-trained fastText word embeddings on a Russian language modeling task. The trained model can then be used by the generate script to generate new sequences of words.

## Data
By default, the training script uses the [Russian Twitter Corpus](http://study.mokoron.com/).

## Usage
1. Make sure Python 3.9 and [Poetry](https://python-poetry.org/docs/) are installed on your machine (I use Python 3.9.7 and Poetry 1.1.13).
2. Clone this repository to your machine.
3. Download data manually from [here](https://www.dropbox.com/s/9egqjszeicki4ho/db.sql) and save it locally (default path is *data/db.sql* in repository's root).
4. Install project dependencies (run this and following commands in a terminal, from the root of cloned repository):
```
poetry install --no-dev
```
5. Run following command to create train and valid datasets:
```
poetry run create_dataset --input-dir <path to file with data> --output-dir <path to folder to save created files> --size <number of records to include in dataset>
```
6. Run train with the following command:
```
poetry run train --input-dir <path to file with data> --save <path to save trained model>
```
You can configure additional options (such as hyperparameters) in the CLI. To get a full list of them, use help:
```
poetry run train --help
```
7. Run generate with the following command:
```
poetry run generate --input-dir <path to file with data> --checkpoint <path to trained model> --prefix <seed word> --length <number of words to generate>
```

## Development

The code in this repository must be linted with flake8, formatted with black, and pass mypy typechecking before being commited to the repository.

Install all requirements (including dev requirements) to poetry environment:
```
poetry install
```
Now you can use developer tools.

Format your code with [black](https://github.com/psf/black) and lint it with [flake8](https://github.com/PyCQA/flake8):
```
poetry run black src
```
```
poetry run flake8 src
```
Type annotate your code, run [mypy](https://github.com/python/mypy) to ensure the types are correct:
```
poetry run mypy src
```

Use [pre-commit](https://pre-commit.com/) to run automated checks when you commit changes.
Install the [hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) by running the following command:
```
poetry run pre-commit install
```
Now pre-commit will run automatically on git commit. To trigger hooks manually for all files use the following command:
```
poetry run pre-commit run --all-files
```

## Acknowledgments
* [corus](https://github.com/natasha/corus) - links to publicly available Russian corpora + API for loading and parsing
* [razdel](https://github.com/natasha/razdel) - sentence segmentation for Russian language
* [compress-fasttext](https://github.com/avidale/compress-fasttext) - pre-trained fastText word embeddings for Russian language
