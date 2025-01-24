##imports
import time

#START
print("🌟 MokéBeast Battle 🌟")

time.sleep(1)
name = input("What is the name of your MokéBeast? ")
time.sleep(3)
type = input("Earth. Fire. Air. Water. Spirit. The 5 types lived in harmony... yada yada. What's your MokéBeast's type?")
time.sleep(1)
specialmove = input("What is your MokéBeast's special move? ")
time.sleep(1)
startingHP = input("What is your MokéBeast's starting health? ")
time.sleep(1)
startingMP = input("What is your MokéBeast's starting magic power? ")
time.sleep(1)
beastdetails = {"name":name, "Type":type, "special move": specialmove, "HP":startingHP, "MP":startingMP}

if beastdetails["Type"].lower() == "earth":
  print("\033[32m", end="")
elif beastdetails["Type"].lower() == "air":
  print("")
elif beastdetails["Type"].lower() == "water":
  print("\033[34m", end="")
elif beastdetails["Type"].lower() == "fire":
  print("\033[31m", end="")
elif beastdetails["Type"].lower() == "spirit":
  print("\033[35m", end="")

time.sleep(4)
for name, value in beastdetails.items():
  print(name + ": " + value)
