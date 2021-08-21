[![PyPI version](https://badge.fury.io/py/p-gen.svg)](https://badge.fury.io/py/p-gen)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)


## About

**Password Generator** is a console utility that allows you to generate passwords based on code phrases and a secret key (seed).

***

## Requirements:
* Python 3+

***

## Installation

### Install `password-generator` via pip:

```console
$ pip install p-gen
```

### Set default values to generator:

* Seed _(Default: MySecretSeed)_: 
```bash
export PGEN_SEED=MyNotDefaultSecretSeed  # Linux / OSX
setx PGEN_SEED MyNotDefaultSecretSeed    # Windows
```

* Password Length _(Default: 18)_:
```bash
export PGEN_LENGTH=18  # Linux / OSX
setx PGEN_LENGTH 18    # Windows
```

* Usage of Special Symbols (0 or 1) _(Default: 1)_:
```bash
export PGEN_USE_SPECIAL_SYMBOLS=1  # Linux / OSX
setx PGEN_USE_SPECIAL_SYMBOLS 1    # Windows
```

That's it!

***

## Usage

Available keywords: `pgen p-gen pass-gen`

### Examples

```commandline
pgen -h

>>>
usage: pgen [-h] [-length LENGTH] [-seed SEED] [-special_symbols {0,1}] CodePhrases [CodePhrases ...]

Generate the passwords.

positional arguments:
  CodePhrases

optional arguments:
  -h, --help            show this help message and exit
  -length LENGTH, -len LENGTH, -l LENGTH
                        length of password
  -seed SEED, -s SEED   secret key to generate unique passwords
  -special_symbols {0,1}, -ss {0,1}
                        use special symbols like "!#$./:;" etc.
```

```commandline
pgen phrase1 phrase2

>>> Your password: {Oj>[n8kQZX}lvYF2Y
```

```commandline
pgen phrase1 phrase2 -ss 0

>>> Your password: Jp9YEGbR4aqutZKafu
```

```commandline
pgen phrase1 phrase2 -l 12

>>> Your password: {Oj>[n8kQZX}
```
