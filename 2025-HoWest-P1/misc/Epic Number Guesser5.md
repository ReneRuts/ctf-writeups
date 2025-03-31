# Epic Number Guesser: 5

## Description
Download the program. All "Epic Number Guesser Game" challenges use the same program. There are five hidden flags within the program—find them(duh)!

To help you identify which flag needs to be submitted, I’ve included a number in each flag.

Example: HCTF-FLAG-1_kfkdfkdfkdf This would be the flag for Epic Number Guesser: 1.

Note: Flags are not case-sensitive.

## Files Provided
"epic.exe" [file](./Epic%20Number%20Guesser/epic.exe)

## Writeups
At the start of executing the file it says `Error: env kinda toxic ngl`

first I tried creating a .venv sadly this wasn't it.

After a while i tried creating a variable called TOXIC, and I set that to "false"
`export TOXIC=false` 

This gives the 5th flag.
## Flag
```
hCTF-FLAG-5_BritNeyBitch
```