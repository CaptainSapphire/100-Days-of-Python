from getpass import getpass
#NAMES
player1 = input("What is the username of player 1? ")
player2 = input("What is the username of player 2? ")
#RULES
know_rules = input("Does both players know the rules (y/n)? ")
if know_rules.lower() == "y":
  print("Good! Let's start the game. ")
if know_rules.lower() == "n":
  print("A classic two-person game. Players start each round by saying, “rock, paper, scissors, shoot!” On “shoot,” each player holds out their fist for rock, flat hand for paper, or their index and middle finger for scissors. Rock crushes scissors, scissors cut paper, and paper covers rock. See who wins each round!")
  print("In our case, r = rock, p = paper, s = scissors.")
else:
  print("What?")
#GAME START
player1_shoot = getpass(player1 + ", what do you choose? ")
player2_shoot = getpass(player2 + ", what do you choose? ")
# rock and scissors
if player1_shoot.lower() == "r" and player2_shoot.lower() == "s":
  print(player1_shoot + " wins!")
#rock and paper
elif player1_shoot.lower() == "r" and player2_shoot.lower() == "p":
  print(player2_shoot + " wins!")
#scissors and rock
elif player1_shoot.lower() == "s" and player2_shoot.lower() == "r":
  print(player2_shoot + " wins!")
#scissors and paper
elif player1_shoot.lower() == "s" and player2_shoot.lower() == "p":
  print(player1_shoot + " wins!")
#paper and rock
elif player1_shoot.lower() == "p" and player2_shoot.lower() == "r":
  print(player1_shoot + " wins!")
#paper and scissors
elif player1_shoot.lower() == "p" and player2_shoot.lower() == "s":
  print(player2_shoot + " wins!")
##ALL CASES WHERE THEY TIE
#rock and rock
elif player1_shoot.lower() == "r" and player2_shoot.lower() == "r":
  print(player1_shoot + " ties with " + player2_shoot)
elif player1_shoot.lower() == "p" and player2_shoot.lower() == "p":
  print(player1_shoot + " ties with " + player2_shoot)
elif player1_shoot.lower() == "s" and player2_shoot.lower() == "s":
  print(player1_shoot + " ties with " + player2_shoot)
else:
  print("Someone gave invalid input. Try again.")

print(player1_shoot)
print(player2_shoot)

#🪨 📄✂️ My very first multiplayer game in Python!!! Day 14 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python
