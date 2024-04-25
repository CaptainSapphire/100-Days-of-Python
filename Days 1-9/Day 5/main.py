#All Variables
q1 = ""
q2 = ""
q3 = ""
q4 = ""
q5 = ""
q6 = ""
#intro
print("Hello there. We need to identify if you are a suspect of the recently escaped prisoners from Arkham Asylum.")

#It begins...
q1 = input("Are you an advocate for plant rights? ")
#Poison Ivy
if q1 == "yes":
  print("suspicious...")
  q1 = input("Can you control plants? ")
  if q1 == "yes":
    print("suspicious...")
    q1 = input("Do you have red hair and a green complexion? ")
    if q1 == "yes":
      print("Then you must be Poison Ivy. Come with me back to Arkum, Harley Quinn's awaiting you. ")
else: 
  #Two Faced
  print("So not Poison Ivy, huh?")
  q2 = input("Is half of your faced burned off? ")
  if q2 == "yes":
    print("suspicious...")
    q2 = input("Do you have a two-headed coin in your hand? ")
    if q2 == "yes":
      print("suspicious...")
      print("Is your name Harvey Dent? ")
      if q2 == "yes":
        print("Two-face, you're coming back to Arkham Asylum with me. ")
  else: 
    #Catwoman
    print("Not Poison Ivy nor Two-face.")
    q3 = input("Do you have an affiliation with cats? ")
    if q3 == "yes":
      print("suspicious")
      q3 = input("Are you a thief? ")
      if q3 == "yes":
        print("You must be catwoman. Cmon, Bats is waiting for you. ")
    else: 
      #Scarecrow
      print("Not Poison Ivy, Two-face, nor catwoman.")
      print("My apologies, so many villians escaped tonight. ")
      q4 = input("Do you have an affiliation with gasses and chemicals, AND somewhat resemble a man of straw? ")
      if q4 == "yes":
        print("Okay Scarecrow, let's go.")
      else: 
        #Harley Quinn
        print("Not SCARECROW EITHER??")
        q5 = input("Are you well educated, and half a close affilitation with the joker, perhaps romantically involved with Poison Ivy or the Joker? ")
        if q5 == "yes":
          print("Harley Quinn, love the makeup. Let's get you back to Arkham Asylum. ")
        else:
          q5 = input("Are you batman's worst nemesis, his enemy, and the unpredictable itself? ")
          if q5 == "yes":
            print("AHA! THE JOKER! LET US GET YOU BACK TO ARKHAM ASYLUM AT ONCE!")
          else:
            print("Okay I give up I don't know WHO you are.")

#Poison Ivy - check
#Two Face - check
#CatWoman - check
#Scarcrow - check
#Harley Quinn - check
#The Joker - check
