# N Queens Algorithm

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Getting started

Make sure you have installed.

- [Python 3.7+](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/)

## Installation

Setup your environment with:

```sh
git clone git@github.com:alfonsorodrigo/n-queen.git
cd n-queen
docker build .
docker-compose build
```

## Testing

To run the tests with the n queens algorithm, execute:

```sh
docker-compose run cuenca_app sh -c "python ./test_n_queen.py"
```

To run the tests saving data in postgresql, execute:

```sh
docker-compose run cuenca_app sh -c "python ./test_n_queen_model.py"
```
