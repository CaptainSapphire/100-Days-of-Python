#basic variables
seconds = 60
minutes = 60
hours = 24
days_year = 365
days_leap_year = 366

#intro
print("Let's find out how many seconds are in a YEAR!")
#Math time!
#Let's find how many are in a day first
hour = seconds * minutes
day = hour * hours

#take into account leap year
leap = input("Is it a leap year (y/n)? ")
if leap == "y":
  year = day * days_leap_year
  print("There are " + str(year) + " seconds in a leap year!")
elif leap == "n":
  year = day * days_year
  print("There are " + str(year) + " seconds in a year!")
else:
  print("Invalid input.")

#How many seconds in a year 🙀 !! Day 11 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python
