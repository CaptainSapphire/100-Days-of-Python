#imports
import random, os, time

#variables
listOfWords = ["science", "mathematics", "engineering", "design", "history", "geography", "health"]
letterPicked = []
lives = 6

word = random.choice(listOfWords)
##START
print("Welcome to hangman! The theme?")
time.sleep(2)
print("School subjects!")

while True:
  time.sleep(1)
  os.system("clear")
  letter = input("Choose a letter: ").lower()

  if letter in letterPicked:
    print("You've tried that already!")
    continue

  letterPicked.append(letter)

  if letter in word:
    print("You found a letter! Yay!")
  else:
    print("Nope, not in our word :)")
    lives -= 1

  allLetters = True
  print()
  for i in word:
    if i in letterPicked:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False
  print()

  if allLetters:
    print(f"You won with {lives} left!")
    break

  if lives<=0:
    print(f"You ran out of lives! The answer was {word}")
    break
  else:
    print(f"Only {lives} left")
