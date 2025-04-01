# cpp of is it js, maybe ps?

## Description
https://letmegooglethat.com/?q=Polyglot

## Files Provided
"polyglot.exe" [file](./cpp%20of%20is%20it%20js,%20maybe%20ps/polyglot.exe)

## Writeups
when running the .exe file it asks for a programming language.

when running `strings polyglot.exe` it shows some pieces of code, however when scrolling down more it gives a list of 10 programming languages which I needed to enter into the program, which ended up in nothing, it just wouldn't give the flag.

List of languages in strings:
`JavaScriptBashPHPJavaC++RustRubyGoPerl`

When looking a bit lower in the program there  was a Base64 string starting with "SENUR" And I already knew that was the starting of base64 strings for `HCTF-FLAG` format strings.

Base64 string: 
`SENURi1GTEFHLUo0dmFTY3JpcHRJc1RoZUdvYXQh`

Decoding that gave me the flag.

## Flag
```
HCTF-FLAG-J4vaScriptIsTheGoat!
```