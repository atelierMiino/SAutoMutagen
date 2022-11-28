# Semi-Auto Music Tagger: sauto_mutagen

## How it Works
This is a quick, small, and low-effort program to organize music which I got from
```
youtube-dl -x YOUTUBE_URL
```
to organize music. It adds basic artist / title metadata to audio
files so when it is played through an audio player, the metadata is
displayed correctly instead of being listed as unknown.
It will rewrite all music metadata in the given directory
AND subdirectories.

Use:
```
python sauto_mutagen.py DIRECTORY
```
to run in a different directory.
* Note: If directory uses spaces, you must use quotations around the directory.

Use:
```
python sauto_mutagen.py
```
to run in current directory.

## Dependencies
* Python3.x
* find UNIX command
* [mutagen](https://mutagen.readthedocs.io/en/latest/)

## Prerequisite Conditions for Program Operation
1. Audio filetype should be supported by the mutagen dependency.
2. Audio filename must be named in the format:
```
AUTHOR - TITLE.FILETYPE
```
* Note: ' - ' is important. Simply using '-' will not suffice.
* Note: Deviating from this format will cause artist to default to 'Unknown Artist' and
title to default to the entire filename (without the filetype)

## Possible Points of Failure
1. Newlines in the middle of the filename may cause the program to operate incorrectly.
2. Unusual nonbinary characters in filename may cause the program to operate incorrectly.