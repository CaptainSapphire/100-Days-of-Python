# Day 26

## Lesson Summary
What is the os library? It allows us to "talk" to the console. One of the most powerful things we can do with this library is allow it to clear the console.
```
os.system("clear")
```
We can import a second library by placing a , after the name of the first library.
👉 Let's add a second library, time.
import os, time
This library allows us to pause the execution of a program for a specific amount of time. The time.sleep(1) function allows us to pause the program for the amount of seconds listed in the ().

## Challenge Directions
Play a song from this repl and build a menu to go with it. Make it look like an iPod!

Use a while true loop to create a title for a music player.
Allow the user to select to play a song and use subroutine called 'play' when they select the song.
Give the user the option to exit the program.
The title should pop up and pause along with the menu options.
If the user chooses anything else, start again by clearing the screen.
Use this code to get started:
```
from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    input()

while True:
  # clear the screen 

  # Show the menu

  # take user's input

  # check whether you should call the play() subroutine depending on user's input
```
