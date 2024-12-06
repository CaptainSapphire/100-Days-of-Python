from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    input()
##START
while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  print("🎵 MyPOD Music Player")
  print("Press 1 to Play")
  print("Press 2 to Exit")
  # take user's input
  userInput = int(input())
  # check whether you should call the play() subroutine depending on user's input
  if userInput == 1:
    play()
  elif userInput == 2:
    break
  else:
    continue
