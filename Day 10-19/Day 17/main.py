from getpass import getpass
#as input

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

#ROUNDS
print("ARE YOU READYYYYYYYY TO RUMBLE???")
print("ROCK, PAPER SCISSORS, FIGHT!!")
print()
print("Select your move (R, P or S)")
print()
#SCORE
player1_score = 0
player2_score = 0
# MAKE YOUR CHOICE!!
while True: 
  player1Move = getpass(player1 + ", what do you choose? "
  print()
  player2Move = getpass(player2 + ", what do you choose? "
  print()
  
  if(player1Move=="R"):
   #rock and rock
    if(player2Move=="R"):
      print("Neither of your rocks are stronger. You shoulda picked a rock made of iron or something, " + player1 + " draw!")
    #rock and scissors
    elif(player2Move=="S"):
      print(player1 +" shattered " + player2 + "'s Scissors  with their Rock!")
      player1_score += 1
    elif(player2Move=="P"):
      print(player1 +"'s Rock is smothered by " + player2 + "'s Paper!")
      player2_score += 1
  elif(player1Move=="P"):
    if(player2Move=="R"):
      print(player2 +"'s Rock is smothered by " + player1 +"'s Paper!")
      player1_score += 1
    elif(player2Move=="S"):
      print(player1 +"'s Paper is cut into tiny pieces by " + player2 + "'s Scissors!")
      player2_score += 1
    elif(player2Move=="P"):
      print("Two bits of paper fall, and slowly float to the ground. LAME! Draw.")
  elif(player1Move=="S"):
    if(player2Move=="R"):
      print(player2 +"'s Rock makes metal-dust out of " + player1 +"'s Scissors")
      player2_score += 1
    elif(player2Move=="S"):
      print("Ka-Ching! Scissors bounce off each other like anime sword fight! Draw.")
    elif(player2Move=="P"):
      print(player1 +"'s Scissors make confetti out of " + player2 +"'s paper!")
      player1_score += 1

#WHO WINS
  print(player1 + " has A GRAND TOTAL OF ", player1_score, " POINTS, and so they win.")
  print(player2 + " has A GRAND TOTAL OF ", player2_score, " POINTS, and so they win.")

  if player1_score==3 or player2_score==3:
    print("Thanks for playing!")
    exit()
  else:
    continue
