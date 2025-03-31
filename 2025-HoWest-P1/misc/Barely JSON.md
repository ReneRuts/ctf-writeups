# Barely JSON

## Description
vgAAAAIwABwAAABBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWi0ABDEAkwAAABAwAAcAAAAQMQACAAAAEDIAEwAAABAzAAUAAAAQNAAaAAAAEDUABQAAABA2AAsAAAAQNwAAAAAAEDgABgAAABA5ABoAAAAQMTAAAQAAABAxMQASAAAAEDEyAA4AAAAQMTMADQAAABAxNAARAAAAEDE1ABQAAAAQMTYACwAAABAxNwAEAAAAEDE4ABIAAAAAAA==

## Files Provided
None

## Writeups
Tried if it was a Base64 string, sadly enough it wasn't.

Looked a bit better at the title of the challenge and searched for BSON, which gave me a [BSON to JSON converter](https://mcraiha.github.io/tools/BSONhexToJSON/bsonbase64tojson.html)

This gives this JSON:
```JSON
{
    "0": "ABCDEFGHIJKLMNOPQRSTUVWXYZ-",
    "1": [ 7, 2, 19, 5, 26, 5, 11, 0, 6, 26, 1, 18, 14, 13, 17, 20, 11, 4, 18 ]
}
```

Converting the numbers to letters using:
- A = 0 
- Z = 25 
- '_' = 26

We get the flag.
## Flag
```
HCTF-FLAG-BSONRULES
```