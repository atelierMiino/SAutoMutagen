# MUSIC-LABELLER: MuLabel

## How it Works
This is a quick, small, and low-effort program to organize music which I got from
```
youtube-dl -x YOUTUBE_URL
```
to organize music. It adds basic artist / title metadata to audio
files so when it is played through an audio player, the metadata is
displayed correctly instead of being listed as unknown.
It will rewrite all music metadata in the given directory
AND subdirectories. Use:
```
python mulabel.py DIRECTORY
```
to run in a different directory. Use:
```
python mulabel.py
```
to run in current directory.

* Note: This program is NOT dummy-proof. Please read the rest of the readme before using.

## Dependencies
* Python3.x
* find UNIX command
* [music_tag](https://github.com/KristoforMaynard/music-tag)

## Prerequisite Conditions for Program Operation
1. Audio filetype should be supported by the music-tag dependency.
2. Audio file must be named in the format:
```
AUTHOR - TITLE
```
* Note: ' - ' is important. Simply using '-' will cause the program to interpret
the entire filename as the title.

## Possible Points of Failure
1. If the filename contains multiple instances of ' - ', program will
fail to work correctly.
2. Spaces in the directory also cause it to fail if passed in the commandline without
quotation marks.
3. The file extensions are case sensitive, meaning if the file was named FILENAME.MP3
instead of FILENAME.mp3, the program may fail to interpret it as a valid audio filetype.
4. Newlines in the middle of the filename may cause the program to operate incorrectly.
5. Unusual nonbinary characters in filename may cause the program to operate incorrectly.

## Room for Improvement
1. Instead of reading the extension for the filetype, the metadata 'type' could be
interpreted instead.