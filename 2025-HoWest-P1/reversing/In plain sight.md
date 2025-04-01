# In plain sight

## Description
None

## Files Provided
"in_plain_sight" [file](./In%20plain%20sight/in_plain_sight)

## Writeups
when running `file in_plain_sight` on the file it shows its a `.elf` file.

Added execution perms & executed the file.

When executing the file it asks for a password.

when running `strings in_plain_sight` it returns a line with `I_should_hide_strings_better` which is the password.

When entering the password it gives the flag.
## Flag
```
HCTF-FLAG-44894
```