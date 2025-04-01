# Assemble the legions

## Description
Assemble the mighty legions of the Emperor to banish the forces of Chaos

The readme is not that trustworthy, trust the program ;)

## Files Provided
"readme.txt" [file](./Assemble%20the%20legions/readme.txt)

"check_dirs.exe" [file](./Assemble%20the%20legions/check_dirs.exe)

## Writeups
from reading the readme.txt file it was pretty clear we had to create a folder structure so [I](https://chatgpt.com) wrote a script that did what was asked inside of the readme.txt:

[The script](./Assemble%20the%20legions/script.py)

When running the check_dirs.exe file It told me it was missing something:
```
In the Grimdark future of the 41st Millennium 
there is only war...
Arise mighty legions of Terra and serve our Emperor
Horus primarch of the Sons of Horus                             ERROR: LEGION IS MISSING, folder Sons of Horus NOT FOUND
Error: Missing legions detected, assemble all legions to go forward!
Find the readme for more instructions!
FOR THE EMPEROR
```
However the folder did exist.

When searching "41st millennium" I stumbled upon something called ["Warhammer 40k wiki"](https://warhammer40k.fandom.com/wiki/Warhammer_40k_Wiki)
Where I noticed there was a typo in the main folders name.

"Adaptus_Astartes" should be "Adeptus_Astartes"

After fixing that and retrying the program it gave me the flag.


Correct working files with executable: [FolderStructure](./Assemble%20the%20legions/Adeptus_Astartes/)
## Flag
```
HCTF-FLAG-ForTheThroneAndEmperor!
```