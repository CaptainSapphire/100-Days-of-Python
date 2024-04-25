#Introduction
username = input("What's your name?")
print("Hello " + username)
day = input("What day of the week is it?")
thingsA = input("What are your favorite hobbies?")
thingsB = input("Another.")
thingsC = input("And last one?")
thingsD = input("Okay oneeee more.")
## Weekdays if-statements
#Monday
if day.lower == "monday":
  print("I think it's so cool that you like " + thingsA)
#Tuesday
elif day.lower == "tuesday":
  print("You're very cool that you like " + thingsA)
#Wednesday
elif day.lower == "wednesday":
  print("It's awesome you have an interest in " + thingsB)
#Thursday
elif day.lower == "thursday":
  print("You are an awesome person, and it's lovely you like " + thingsB)
#Friday
elif day.lower == "friday":
  print("You're lovely for being intersted in " + thingsC)
#Saturday
elif day.lower == "saturday":
  print("It's amazing you like" + thingsC)
#Sunday
elif day.lower == "sunday":
  print("You're amazing for being interested in " + thingsD)
#Else
else:
  print("Sorry, I don't understand.")

#Final challenge included with the .lower function in the if statements
#I really enjoyed this challenge, affirmations are awesome :)
