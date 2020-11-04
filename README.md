# Music-Player-In-Python
Simple music player in python made using the simpleaudio package. Coded in Norwegian, programmed using python.

Required to use the simple audio package:

pip install simpleaudio

more info on the package here: https://simpleaudio.readthedocs.io/en/latest/installation.html

## How to use
create a folder named 'music' (case sensetive) and put all the .wav files you want, run the program using 'sangtester.py', the program runs true the music folder finds any .wav files and represents them in the program, you can then choose what song to play and it will play. If you have folders inside the music folder no worries the program will search true them aswell and save any .wav files so you can play them in the program.

### Understanding the folder system
If you put folders inside the 'music' folder they will act like albums, each folder will be the albumname and it's songs will be the .wav files inside folder

### Features
* A main playlist for all the music in the 'music folder'
* Folders inside 'music' folder will automatically be converted to albums that have the corrensponding songs in them as the .wav files inside the folders.
* Play any .wav file

### Restrictions
This works with only .wav files, simpleaudio does not support .mp3, .flac or any other file format.

The program expect you to put in valid input when asked. This can cause errors if the user types in something that is not a command for the program.

If the folder/album has no .wav files, the program will tell you.
