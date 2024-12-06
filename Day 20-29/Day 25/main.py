import random
print("⚔️ Character Stats Generator ⚔️")
##Then, create a second subroutine that rolls one six-sided dice and one eight-sided dice.
def diceRoll2(number):
  dice6 = "" 
  dice8 = "" 
  for i in range(number): 
    dice6 += str(random.randint(1,6)) 
    dice8 += str(random.randint(1,8)) 
  ##Multiply the number from the six-sided dice and eight-sided dice together and return that subroutine as a character's health stats for a video game.
  dicereturn = int(dice6) * int(dice8)
  return dicereturn

##Print out the character's health stats.
myroll = diceRoll2(1)
charname = input("Name your hero: ")
print("Their health is: ", str(myroll) + "hp")
##Add a loop to give the user the option to generate health stats for another character.
while True:
  myroll = diceRoll2(1)
  charname = input("Name your hero: ")
  print("Their health is: ", str(myroll) + "hp")

  another = input("Do you want to generate health stats for another character? (yes/no): ")
  if another.lower() != 'yes':
      break
