##START
print("Name the Lyrics GAME!")
print("Fill in the blank lyrics!")
print("(Type in the blank lyrics and see if you are as cool as me.)")
#The while-true
count = 0
while True:
  lyrics = input("Never going to ______ you up.")
  if lyrics == "give":
    break
  else:
    print("Nope, try again.")
    count = count + 1
print("Well done! It only took you " + str(count) + " attempts.")


#Can you guess the lyrics to a worldwide favorite song 🎶 🎤?  Day 16 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python
