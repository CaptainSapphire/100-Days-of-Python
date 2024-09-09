import random

#Variables
variable1 = random.randint(0, 1000000) #i got lazy with the name
attempt = 1
#START
print("#️⃣  WELCOME TO GUESS THE NUMBER #️⃣")
print("Guess a number between 1 && 1,000,000 and I will tell you where your guess falls... :)")
print()
print("Let's play!")
guess = int(input("Guess the number: "))
while (guess != variable1):
  if (guess < 0):
    print("You can't guess a negative number!")
  else:
    if (guess > variable1):
      print("Too high")
    if (guess > variable1):
      print("Too high, fruit fly 🍒✈️")
    #The fly emoji does not work on replit
    elif (guess < variable1):
      print("Too low, big toe 🦵🦶")
    guess = int(input("Guess the number: "))
    attempt = attempt + 1

if (guess == variable1):
  print("You guessed the number!🥳👏👏🎊")
  print("It took you ", attempt, " attempts to guess the number.")
