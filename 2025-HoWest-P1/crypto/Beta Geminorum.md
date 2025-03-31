# Beta Geminorum

## Description
An eccentric cryptographer once devised a method of encryption inspired by the unpredictable nature of celestial twins. By blending structure with randomness, their cipher ensures that the same message may never appear the same way twice.

Can you decipher the stellar code and reveal the flag?

KKKKJCBLBJCIBKCKJ-BBLBIBLBKIKLJCLBJ-LBBBIKCBJBBICCBIBKKBJCIBIBBBJLJLIKCLIKBICKJ

FAAFHEFEADGDAFGFD-AFEADAEFFDAEDGGFH-EAAADFGAHFFHGGAHAAAFHGDAHFFAHGDGHAEGDFFDGFD

(You'll have to manually add the -'s the flag)

## Files Provided
None

## Writeups
Tried a lot of things but didn't find anything.

Then had a Challenge with Morse inside of it, which made us think. What if we look for HCTF in morse inside of this one.
Only 1 part of the string is Needed after this hint. 

If we take the bottom part of the string and get what characters are in there
we get:
- F
- A
- H
- E
- D
- G

Where:
- A & F are a "."
- D & H are a " " (space)
- E & G are a "-"

When trying this on the part of the given string before the first "-"

it gave us this in morse:
```
.... -.-. - ..-.
```
Which is "HCTF"

We now found the flag by doing this for the whole string.

1. 
    Morse: .... -.-. - ..-.

    Normal text: HCTF

2. 
    Morse: ..-. .-.. .- --.

    Normal text: FLAG

3. 
    Morse: -... .-. .. --. .... - . ... - - .-- .. -.:
    
    Normal text: BRIGHTESTWIN

## Flag
```
HCTF-FLAG-BRIGHTESTWIN
```