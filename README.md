# Sermepa client

[![Build Status](https://travis-ci.org/Som-Energia/sermepa.svg?branch=master)](https://travis-ci.org/Som-Energia/sermepa)

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

### sermepa 1.0.0

- Suport for Python3
- Breaking change: all input and output strings of the library are expected to be unicode, not bytes
    - To ease transition whenever a parameter is sent as bytes, utf8 decoding is enforced
- Accept `Ds_Merchant_Cof_Txnid` parameter set

### sermepa 0.1.3

- Accept `Ds_Card_Type` parameter set
- Accept `Ds_Card_Brand` parameter set
- Accept `Ds_ErrorCode` parameter set

### sermepa 0.1.2

- Adapted to the new 256 encryption schema
- Full unittesting
- Specification tables copied into code


### sermepa 0.1.1

- First version by Gisce

## TODO

- Accept all new parameters in specification 
- Recover pypi project
- Review error handling
- Production api test should depend on the concrete key

