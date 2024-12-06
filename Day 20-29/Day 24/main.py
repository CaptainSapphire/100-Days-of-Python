#functions
#x is sides
def roll(x):
  rollnum = random.randint(1, x)
  print("You rolled " + str(rollnum))

#START
import random
print("Infinity Dice 🎲")

sides = int(input("How many sides?: "))
numberofrolls = int(input("How many rolls?: "))

for i in range (numberofrolls):
  roll(sides)

