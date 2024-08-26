#STEP 1
test = input("What is the name of the test? ")
max = int(input("What is the maximum score? "))
score = int(input("What score did you receive? "))

#STEP 2
percent = round(score / max * 100, 2)
#STEP 3
if percent >= 90:
  print("You got an A+! That's incredible!! 👏👏👏")
elif percent >= 80:
  print("You got an A! That's amazing, congrats.👏👏")
elif percent >= 70:
  print("You got an B! Beeeee happy about that, since it's great. 🐝")
elif percent >= 60:
  print("You got an C! It's passing, seeeee?! 🇨")
elif percent >= 50:
  print("You got a D! Could be worse! 🤷")
elif percent >= 50:
  print("You got a F! uh... oh. 🫢")

  #Built a grade calculator today! Definitely giving myself an A+ on this 😎 ! Day 13 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python
