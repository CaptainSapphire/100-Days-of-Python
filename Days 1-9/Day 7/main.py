#My idea divulged from the prompt, I know, but I really wanted to do something like this, especially bc I am not a mega fan of anything in particular. 
#Variables
favGift = ""
single = ""
easterq = ""
fourthq = ""
halloq = ""
#START
holiday = input("What is your favorite holiday?(do not include day in your answer.) ")
#Christmas
if holiday.lower == "christmas":
  print("Good choice! Deck the halls to make it appear as a Winter Wonderland and enjoy a fun Sleigh Ride! (I tried).")
  faveGift = input("What's your favorite type of gift? ")
  if faveGift == "clothes":
    print("So you're over 18. Nice.")
  elif faveGift == "toys":
    print("Hi kiddo.")
  else:
    print("Good choice.")
#New Years
elif holiday.lower == "new years":
  print("Why? WHY??")
#Valentines
elif holiday.lower == "valentines":
  single = input("Are you single?")
  if single.lower == "yes":
    print("how sweet.")
  elif single.lower == "no":
    print("Then...Why??")
  else:
    print("huh?")
#Easter
elif holiday.lower == "easter":
  print("Chocolate galore!")
  easterq = input("What's your favorite part of easter?")
  if easterq.lower == "chocolate":
    print("Makes sense, me too.")
  elif easterq.lower == "easter eggs":
    print("I guessssss.")
  elif easterq.lower == "easter bunny":
    print("Yeah so...WHY? I feel a rabbit that lays eggs made of plastic filled with chocolate for children perhaps is a stranger concept.")
  else:
    print("Okay.")
#Independence Day
elif holiday.lower == "independence":
  print("O say can you see by the dawn's early light-")
  print("I'm American too.")
  fourthq = input("What's your favorite part of Independence Day?")
  if fourthq.lower == "the holiday":
    print("That was the most boring possible answer. Bruh.")
  elif fourthq.lower == "fireworks":
    print("I agree! I love seeing the colorful fireworks.")
  elif fourthq.lower == "america":
    print("O say can you see by the dawn's early light")
    print("What so proudly we hailed at the twilight's last gleaming")
  else:
    print("nice")
#Thanksgiving
elif holiday.lower == "thanksgiving":
  print("Fooooood.")
#Veterans Day
elif holiday.lower == "veterans":
  print("Repectable.")
#Holi
elif holiday.lower == "holi":
  print("I love the festival of colors!")
#Diwali
elif holiday.lower == "diwali":
  print("I love the festival of lights!")
#Hannukah
elif holiday.lower == "hannukah" or holiday.lower == "rosh hashannah" or holiday.lower == "yom kippur":
  print("Judaism, very awesome.")
#Saint Patricks day
elif holiday.lower == "st. patrick's":
  print("Nice... I mean, of all the holidays, that's... one of them.")
#Halloween
elif holiday.lower == "halloween":
  print("BOO! I love halloween as well!")
  halloq = input("What your favorite part of halloween?")
  if halloq.lower == "candy":
    print("Heya kiddo. Good choice for now.")
  elif halloq.lower == "costumes":
    print("So fun, isn't it?")
  elif halloq.lower == "trick or treating":
    print("So what do you choose? :)")
  elif halloq.lower == "parties":
    print("I love parties!")
#Black Friday
elif holiday.lower == "black friday":
  print("Gotta love those sales!")
else:
  print("Yeah, that's cool!")
