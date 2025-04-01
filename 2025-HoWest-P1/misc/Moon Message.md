# Moon Message

## Description
NASA was going to send me some pictures of the moon, but all I got was this banger beat.

(Don't attack the filesender! It's just to get the message.wav)

## Files Provided
"message.wav" [file](./Moon%20Message/message.wav)

## Writeups
I first tried listening to hear if I could find something, sadly I didn't.

Then I went to Kali Linux to try and run some commands on it.

- file message.wav
- xxd message.wav message.hex
- exiftool -e message.wav

all without any result.

When looking a bit at the description and stuff I started wondering how NASA does sent pictures from the moon to earth

After a while I stumbled upon something called "SSTV" aka "Slow Scan TeleVision"

Then I started searching for a decoder and found this one: [decoder](https://github.com/colaclanth/sstv.git)

I installed this on my Kali Linux and tried the command on the file.

Which output a file with the flag inside of it.

## Flag
```
HCTF-FLAG-TOTHEMOON
```