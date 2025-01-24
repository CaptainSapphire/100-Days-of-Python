#global variables
toDoList = []
exit = ""

#Functions
def printList():
    print()
    for item in toDoList:
        print(item)
    print()

def check_duplicates(input_list):
    if len(input_list) != len(set(input_list)):
        return True  
    else:
        return False

#imports
import os, time

##START
print("To Do List Manager:")

while exit != "yes":
    ask = input("1: View items\n2: Add item\n3: Clear items\n4: Edit item\n> ")

    if ask == "view":
        if not toDoList:
            print("There are no items on this list.")
        else:
            printList()
        exit = input("Would you like to exit? (yes/no): ")
        os.system("clear")

    elif ask == "add":
        item = input("What do you want to add? ")
        if check_duplicates(toDoList + [item]):
            print("Duplicate item! cannot add to the list.")
        else:
            toDoList.append(item)
            printList()
        exit = input("Would you like to exit? (yes/no): ")
        os.system("clear")

    elif ask == "edit":
        if not toDoList:
            print("There are no items to edit.")
        else:
            old_item = input("Which item do you want to edit? ")
            if old_item in toDoList:
                index = toDoList.index(old_item)
                new_item = input("Enter the new item: ")
                toDoList[index] = new_item
                print("Item edited successfully.")
                printList()
            else:
                print("Item not found in the list.")

        exit = input("Would you like to exit? (yes/no): ")
        os.system("clear")

    elif ask == "clear":
        toDoList.clear()
        print("List cleared.")
        exit = input("Would you like to exit? (yes/no): ")

    else:
        print("❓❓Invalid input. Try again.❓❓")
