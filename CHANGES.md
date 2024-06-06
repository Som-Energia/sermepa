# Changelog

## sermepa 1.1.0 (2024-06-06)

- Support `Ds_Merchant_PayMethod` to use Bizum, PayPal...

## sermepa 1.0.4 (2021-12-22)

- When sermepa revice an unexpected param in `decodeSignedData` method not will raise `SignatureError`

## sermepa 1.0.2 (2020-09-16)

- Accept `Ds_ProcessedPayMethod` parameter set

## sermepa 1.0.1 (2020-06-16)

- Packaging issues to upload onto pipy

## sermepa 1.0.0

- Suport for Python3
- Breaking change: all input and output strings of the library are expected to be unicode, not bytes
    - To ease transition whenever a parameter is sent as bytes, utf8 decoding is enforced
- Accept `Ds_Merchant_Cof_Txnid` parameter set

## sermepa 0.1.3

- Accept `Ds_Card_Type` parameter set
- Accept `Ds_Card_Brand` parameter set
- Accept `Ds_ErrorCode` parameter set

## sermepa 0.1.2

- Adapted to the new 256 encryption schema
- Full unittesting
- Specification tables copied into code


## sermepa 0.1.1

- First version by Gisce

## TODO

- Accept all new parameters in specification 
- Recover pypi project
- Review error handling
- Production api test should depend on the concrete key

