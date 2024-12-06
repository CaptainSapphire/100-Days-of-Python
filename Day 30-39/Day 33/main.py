#global variables
toDoList = []

#Functions
#this was taken from the example code
def printList():
  print() #this is just to add an extra space between items
  for item in toDoList:
    print(item)
  print() #this is just to add an extra space between items

#imports
import os, time

##START
print("To Do List Manager:")
#ask = input("Do you want to view, add, or edit your to do list?")

while exit != "yes":
  ask = input("Do you want to view, add, or edit your to do list?")
  if ask == "view":
    if toDoList == []:
      print("There are no items on this list.")
      exit = input("would you like to exit✖️?")
    else:
      printList()
      exit = input("would you like to exit✖️?")
    os.system("clear")
  elif ask == "add":
    #append to the list
    item = input("What do you want to add?")
    toDoList.append(item)
    printList()
    exit = input("would you like to exit✖️?")
    os.system("clear")
  elif ask == "edit":
    #remove from the list
    if toDoList == []:
      print("There are no items on this list.")
      exit = input("would you like to exit✖️?")
    else: 
      item = input("What do you want to remove?")
      toDoList.remove(item)
      printList()
    os.system("clear")
  else:
    print("❓❓Invalid input. Try again.❓❓")


