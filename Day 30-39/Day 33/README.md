# Day 33

## Lesson Summary
Dynamic lists are ways of using a blank list and adding or removing items to it as we go.

Blank lists
```
myAgenda = []
```

Append a list
.append will let us add whatever is in () to the list.

Removing items from a list
```
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    myAgenda.remove(item)
  printList()
```

## Challenge Directions
Create your own to do list manager. (This can be super useful!)

Ask the user whether they want to view, add, or edit their to do list.
If they want to view it, print it out in a nice way (Hint: subroutine).
If they choose to add an item to the to do list, allow them to type in the item and then add it to the bottom of the list.
If they want to edit the to do list, ask them which item they completed, and remove it from the list.
Don't worry about duplicates!
The first item you put in the list should be the first item you remove.
Add a title, some color, alignment to the text, or emojis. Show off your skills!
Example:
```
To Do List Manager:
Do you want to view, add, or edit your to do list?
view

Record video for day 34
```
