##I wanted to play with emojis for this one, did not do the animal sounds, did emojis instead.

#The function
def emojicheck(emoji):
  if emoji.lower() == "laugh":
    print("😂")
  elif emoji.lower() == "heart-eyes":
    print("😍")
  elif emoji.lower() == "sob":
    print("😭")
  elif emoji.lower() == "sob":
    print("🥺")
  elif emoji.lower() == "sunglasses":
    print("😎")
  elif emoji.lower() == "nerd":
    print("🤓")
  
#The loop
while exit != "yes":
  print("Options for emojis: laugh, heart-eyes, sob, plead, sunglasses and nerd!")
  emoji = input("What emoji do you want to see?")
  emojicheck(emoji)
  exit = input("Do you want to exit?")


#DO NOT USE but here it is: What does the 🦊 say ? Find out with my custom animal sound generator (just like Alexa)! Day 15 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python
