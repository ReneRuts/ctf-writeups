# Ragex

## Description
I've lost my flag in this mess...

All i remember is that

The flag starts with HCTF-FLAG- and is followed by a value encapsulated within curly braces { }
The content inside the {} consists of uppercase letters and underscores
The content inside the {} begins with an uppercase letter (not an underscore)
The length of the content inside {} is between 15 and 25 characters
Can you help me find it?

## Files Provided
"mess.txt"

## Writeups
The contents of the [file](./Ragex/mess.txt) contains a lot of flags.

The flag starts with HCTF-FLAG- and is followed by a value encapsulated within curly braces { }
- added `HCTF-FLAG\{\}` to the regex. (Backslashes are to ensure the litteral braces)
The content inside the {} consists of uppercase letters and underscores
- added `[A-Z_]` to the regex.
The content inside the {} begins with an uppercase letter (not an underscore)
- added `[A-Z]` to the front inside the curly braces.
The length of the content inside {} is between 15 and 25 characters
- added `{14,24}` to the end of the regex inside the curly braces.
Can you help me find it?


The correct flag can be found with the following regex.
`HCTF-FLAG-\{[A-Z][A-Z_]{14,24}\}`

## Flag
```
HCTF-FLAG-{YOU_FOUND_THE_NEEDLE}
```