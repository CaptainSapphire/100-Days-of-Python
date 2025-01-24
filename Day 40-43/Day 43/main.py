## I don't think I ever completed this one. 

import random

bingo = []

def ran():
  #Randomly generate a series of number between 0 and 90.
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    print(row)

numbers = []
for i in range(8):
  numbers.append(ran())

numbers.sort()

#Allocate each number to a place in a 2D list.
bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]
prettyPrint()
