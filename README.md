# Sermepa client


[![CI Status](https://github.com/Som-Energia/sermepa/actions/workflows/main.yml/badge.svg)](https://github.com/Som-Energia/sermepa/actions/workflows/main.yml)
[![PyPi Downloads](https://img.shields.io/pypi/dm/sermepa.svg)](https://pypi.python.org/pypi/sermepa)
[![Coverage Status](https://coveralls.io/repos/github/som-energia/sermepa/badge.svg?branch=master)](https://coveralls.io/github/som-energia/sermepa?branch=master)

A python client library for sending payment orders to the Sermepa/RedSys payment service.

## Installation

From pypi.org

```bash
pip install sermepa
```

From source:
```bash
pip install .
```

## Running tests

```bash
$ ./setup.py test
```

If you want to test your own keys create file `config.py`
with:

```python
# This one should be your private one
redsys = dict(
   merchantcode = '123456789',
   merchantkey = 'blablablablablablablablablabla',
)

# This is a common one but you can have your own test key
redsystest = dict( # Clave para tests
   merchantcode = '999008881',
   merchantkey = 'sq7HjrUOBfKmC576ILgskD5srU870gJ7',
)
```

## Changelog

[CHANGES.md](CHANGES.md)

## TODO

- Accept all new parameters in specification 
- Recover pypi project
- Review error handling
- Production api test should depend on the concrete key

