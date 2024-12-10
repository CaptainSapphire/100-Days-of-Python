# Day 34

## Lesson Summary

### Pretty print
```
import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") # start by clearing the screen
  print("listofEmail") # print the title of my program
  print() # print a blank line
  for email in listOfEmail: # use for loop to access list
    print(email)
  time.sleep(1)

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
    prettyPrint()  
  time.sleep(1)
  os.system("clear")
```
### Creating a numbered list
```
import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  counter = 1 
  for email in listOfEmail: 
    print(f"{counter}: {email}") 
    counter += 1 
  time.sleep(1)
  
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3": # we added this elif
    prettyPrint() # called our subroutine here
  time.sleep(1)
  os.system("clear")
```
### index
We can also use loops in a slightly different way to access elements in a list (or array). With the way we have our code written right now, our list creates a variable called email, sets it equal to the first value (with our counter we set 1 as the first value), and then counts on as we go. (2, 3, 4, etc.)

However, we can also set the for loop to use the index. What should happen is index will start at 0, go through the entire code in the loop at 0, go back to the start of the loop, add 1, and then loop again and again until the list ends.....

## Challenge Directions
Let's extend this program and build option 4: "Get SPAMMING".

Print out the first 10 email addresses with a custom email sent to each of those people.
Print one email at a time, pause, and then clear the screen before the next email is printed.
Example:
```
Dear john@test.com
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
Ian Spammington III
```
