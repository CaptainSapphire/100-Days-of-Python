#Start
amount = float(input("What is the total bill amount?"))
tip = float(input("What is the tip percentage?"))
#Calucate tip
tip_amount = amount * (tip/100)
#Calculate total
total = amount + tip_amount

#Split the bill
split = input("Are people splitting the bill (y/n)? ")
while split != "y" or split != "n":
  if split == "y":
    numberOfPeople = int(input("How mant people are splitting the bill? "))
    answer = total/numberOfPeople
    print("Each individual owes " + str(answer) + " .")
    break
  elif split == "n":
    print("Alrighty, have a lovely day/night!")
    break
  else:
    split = input("Are people splitting the bill (y/n)? ")


#Built my own tip calculator! Time to put it to the test at a restaurant 🍕 !  Day 10 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python
