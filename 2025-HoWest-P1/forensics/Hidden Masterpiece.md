# Hidden Masterpiece

## Description
I've tucked away my favorite cinematic scene deep inside this image, and, oh, there's a flag hidden in there too... I guess. Can you find it?

## Files Provided
"Cinema.png"

## Writeups
In the description it says us there is something hidden inside the image. 

Went to [CyberChef](https://gchq.github.io/CyberChef/#recipe=Extract_Files(true,false,false,false,false,true,false,true,100)) and tried the "Extract Files" at the bottom of that output there was a .zip file. When downloading that and previewing it it showed a `hint.txt` & `MrWhite.jpg` file.

When reading the `hint.txt` file it said: `Mr White is known to hide his secrets, if only there was a way to inspect the metadata of this image.`

After reading the hint that told us to inspect the metadata I ran `exiftool MrWhite.jpg` which at the description of the image gives the flag.

## Flag
```
HCTF-FLAG_CONTAMINATION
```