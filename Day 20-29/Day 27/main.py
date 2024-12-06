##Note: I changed some of the directions for creative liberties :)
#- I used time and os to make the program more user friendly rather than a menu given it won't work well in this format (the solution didn't make a menu either)
#- I added more species
#- I made all aspects outside of the name random instead of making the user pick the species
#- I added some personalization/comments to make it fun :)
#-------------------------------
#Imports
import random, os, time
##FUNCTIONS
def chargenerate():
  ##Decide type/race of character
  type_list = ["human", "elf", "wizard", "orc", "extraterrestrial", "vampire", "zombie"]
  random_index = random.randint(0, len(type_list) - 1)
  character_type = type_list[random_index]
  return character_type
def healthgenerate():
  ##Decide health of character
  dice_6 = random.randint(1, 6)
  dice_12 = random.randint(1,12)
  health = (dice_6 * dice_12)/2 + 10
  return health
def strengthgenerate():
  ##Decide strength of character
  dice_6 = random.randint(1, 6)
  dice_12 = random.randint(1,12)
  strength = (dice_6 * dice_12)/2 + 10
  return strength

#START
print("Welcome! Come make your own character!")
time.sleep(1)
print("You get to pick the name, but, the drawback is that WE pick the rest. :) ")
##Decide name of character
name = input("Name your character: ")
print("Waaaaait....")
time.sleep(1)
print("We are generating itttt (the suspense is killing me)")
time.sleep(2)
print(name + " is a(n)", chargenerate())
time.sleep(0.5)
print("HEALTH: " + str(healthgenerate()))
time.sleep(0.5)
print("STRENGTH: " + str(strengthgenerate()))
time.sleep(0.5)
print()
#Another?
another = input("Would you like to make another? ")
os.system("clear")
while another == "yes":
  name = input("Name your character: ")
  print("Waaaaait....")
  time.sleep(1)
  print("We are generating itttt (the suspense is killing me)")
  time.sleep(2)
  print(name + " is a(n)", chargenerate())
  time.sleep(0.5)
  print("HEALTH: " + str(healthgenerate()))
  time.sleep(0.5)
  print("STRENGTH: " + str(strengthgenerate()))
  time.sleep(0.5)
#Another?
  print()
  another = input("Would you like to make another? ")
  os.system("clear")
else:
  print("May your hero write history...")
