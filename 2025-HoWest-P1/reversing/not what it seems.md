# Not what it seems

## Description
None

## Files Provided
"not_what_it_seems.exe"

## Writeups
When running the file on windows there's an error that says 'not for this windows version.'

When running `file not_what_it_seems.exe` it says it's an MS DOS file.

However when running `strings not_what_it_seems.exe` it says something about linux.

When doing xxd and  changing the magic bytes from `MZ.F` to `.ELF` and then executing the file again it gives the flag.

## Flag
```
HCTF-FLAG-65951
```