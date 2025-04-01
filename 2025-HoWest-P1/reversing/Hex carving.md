# Hex carving

## Description
None

## Files Provided
"hexcarving.txt" [file](./Hex_carving/hexcarving.txt)

## Writeups
Contents of hexcarving is too big to copy paste here. Challenge file in folder `Hex_carving`

When converting the [hex to ascii](https://www.rapidtables.com/convert/number/hex-to-ascii.html)

it returns a file with mostly "This is byte nr :" with in front of the ":" a number lower than 7.

when replacing this in vscode in a file with this regex: `This is byte nr \d:`
It shows an ascii art with the flag.

[ascii-art](Hex_carving/hexCarvingSolution.txt)

## Flag
```
HCTF-FLAG-CARVED_OUT_!
```