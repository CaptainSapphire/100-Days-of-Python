# Day 36

## Lesson Summary

### String Manipulation
.lower = all letters are lower case
.upper = all letters are upper case
.title = capital letter for the first letter of every word
.capitalize = capital letter for the first letter of only the first word
Adding .strip() removes any spaces on either side of the word.
### Removing Duplicates
original:
```
myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  addItem = input("Item > ")
  if addItem not in myList:
    myList.append(addItem) 
  printList()
```
example:
```
myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  addItem = input("Item > ").capitalize().strip()
  if addItem not in myList:
    myList.append(addItem)
  printList()
```

## Challenge Directions
- Create a list of people's names. Ask for first and last name (surname) separately.
- Strip any extra spaces.
- Store names in a capitalized version.
- Create a new string using an fString that combines the tidied up version of the first name and tidied up version of the last name.
- Add those new versions to a list.
- Do not allow duplicates.
- Each time you add a new name, you should print out the full list.
