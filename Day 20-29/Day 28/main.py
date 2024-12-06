#Hello thank you for checking this out :D
#-------------------------------
#Imports
import random, os, time, sys
##FUNCTIONS
def chargenerate():
  ##Decide type/race of character
  type_list = ["human 🧍", "elf 🧝", "wizard 🧙", "extraterrestrial 👽", "vampire🧛🦇", "zombie🧟", "fairy 🧚", "demon 👹", "goblin 👺"]
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

def printstats(name, health, strength):
  print("Name: " + name)
  print("HEALTH: " + health)
  print("STRENGTH: " + strength)

#Global Variables
heroscore = 0
villainscore = 0
strengthdifference = 0
herolines = ["AND THE HERO SLAMS THE VILLAIN WITH AN UPPERCUT!!!👊👊👊","AND THE HERO SMASHES THE VILLAIN WITH A HAMMER!!!🔨🔨","AND THE HERO SLASHES THE VILLAIN WITH A SWORD!!!🗡️🗡"]
villainlines = ["SLASH! THE VILLAIN CUTS INTO THE HERO WITH THEIR WEAPON!! ⚔️⚔️⚔️⚔️", "THE VILLAIN SLAMS THE HERO INTO THE GROUND WITH THEIR WEAPON!! ⚔", "KAPOW! THE VILLAIN WHIPS OUT A SUPERWEAPON THAT EXPLODES ON THE HERO!💣💣"] 
#START
print("Welcome to the battle stage! Here, you will create your hero and villain.⚔️")
time.sleep(1)
print("You get to pick the name, but, the drawback is that WE pick the rest.😈")
##Hero Stats
hero = input("Name your HERO: ")
time.sleep(.5)
print("Waaaaait....")
time.sleep(1)
print("We are generating itttt (the suspense is killing me)")
time.sleep(2)
herospecies = chargenerate()
print(hero + " is a(n)", herospecies)
time.sleep(0.5)
herohealth = str(healthgenerate())
print("HEALTH: " + herohealth)
time.sleep(0.5)
herostrength = str(strengthgenerate())
print("STRENGTH: " + herostrength)
time.sleep(0.5)
print()
#Villain Stats
villain = input("And who is our villain for tonight? ")
print("Waaaaait....")
time.sleep(1)
print("We are generating itttt (the suspense is killing me)")
time.sleep(2)
villainspecies = chargenerate()
print(villain + " is a(n)", villainspecies)
time.sleep(0.5)
villainhealth = str(healthgenerate())
print("HEALTH: " + villainhealth)
time.sleep(0.5)
villainstrength = str(strengthgenerate())
print("STRENGTH: " + villainstrength)
time.sleep(0.5)

###Day 28
time.sleep(2)
os.system("clear")
time.sleep(2)
print("It's time for battle!⚔️")
time.sleep(.5)
# Use a for loop to simulate three rounds of battle.
for round_num in range(1, 4):
    print("\nRound", round_num)
    # Roll one six-sided dice for both characters. The character who rolls the higher amount wins that round.
    dicerollhero = random.randint(1, 6)
    dicerollvillain = random.randint(1, 6)
    #HERO wins this round
    if dicerollhero > dicerollvillain:
        print(random.choice(herolines))
        heroscore += 1
        strengthdifference = float(herostrength) - float(villainstrength) + 1
        villainhealth = float(villainhealth) - strengthdifference
        time.sleep(2)
        printstats(hero, str(herohealth), str(herostrength))
        time.sleep(2)
        printstats(villain, str(villainhealth),str( villainstrength))
        time.sleep(2)
        if villainhealth <= 0:
          os.system("clear")
          print("\033[32mCONGRATULATIONS! " + hero + " WINS!🎉🎉")
          sys.exit()
    #VILLAIN wins this round
    else:
        print(random.choice(villainlines))
        villainscore += 1
        strengthdifference = float(villainstrength) - float(herostrength) + 1
        herohealth = float(herohealth) - strengthdifference
        time.sleep(2)
        printstats(hero, str(herohealth), str(herostrength))
        time.sleep(2)
        printstats(villain, str(villainhealth),str( villainstrength))
        time.sleep(2)
        if herohealth <= 0:
          os.system("clear")
          print("\033[32mCONGRATULATIONS! " + villain + " WINS!🎉🎉")
          sys.exit()
    os.system("clear")
#To keep this battle from looking hideous between rounds use time.sleep to pause between rounds os.system("clear") to ensure the screen clears between battles.
print("Oh my! It's the end of the battle!")
time.sleep(.5)
print("It's time to see who won!")
time.sleep(5)
print("☁️☁️☁️☁️☁️")
time.sleep(2)
print("(Give it a sec, the fog needs to clear)")
time.sleep(.5)
# Check the final health of each character to determine the winner
if float(herohealth) > float(villainhealth):
    print("\n\033[32mAfter 3 rounds, " + hero + " is the ultimate winner with more remaining health!" + "🎉")
elif float(herohealth) < float(villainhealth):
    print("\n\033[32mAfter 3 rounds, " + villain + " emerges victorious with more remaining health!" + "🎉")
else:
    print("\n\033[32mAfter 3 rounds, it's a draw! Both characters have equal remaining health." + "🎉")

#Extra points for the use of emojis, colors, or even sound code!
