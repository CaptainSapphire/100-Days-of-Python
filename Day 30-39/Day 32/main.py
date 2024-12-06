#imports
import random

#In order: english, spanish, gujarati/hindi, german(?), italian/latin, japan, portugese, russian
language = ["Hello","Hola","Chemcho","Bonjour","Guten Tag","Salve","Konnichiwa","Ola","Privet"]
#fun fact! I am learning/speak spanish and gujarati!


randomnumber = random.randint(0,8)
print(language[randomnumber], end = "\n")
print("That means greetings!")

#Use an f-string
