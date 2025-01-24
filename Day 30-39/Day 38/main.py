#imports
import time

##START
#Ask the user to input any sentence (string).
sentence = input("Enter a sentence: ")
print("", end='')

#Loop through the string and output it (so the color continues through the loop).
# The output should change color every time it encounters a new r, g, b, p or y.
for letter in sentence: 
    if letter.lower() == "r":
        print('\033[31m' + letter + "\033[0m", end ="") #red
    elif letter.lower() == "o":
        print('\033[33m' + letter+ "\033[0m", end ="") #orange
    elif letter.lower() == "y":
        print('\033[33m' + letter+ "\033[0m", end ="") #yellow
    elif letter.lower() == "g":
        print('\033[32m' + letter+ "\033[0m", end ="") #green
    elif letter.lower() == "b":
        print('\033[34m' + letter+ "\033[0m", end ="") #blue
    elif letter.lower() == "p":
        print('\033[35m' + letter+ "\033[0m", end ="") #purple
    else:
        print(letter, end="")
    time.sleep(1)

# Reset color after printing the full sentence
print('\033[0m')
time.sleep(1)



