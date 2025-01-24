#globals
list = []

#START
go = input("Would you like to add a person to the list?")
while go.lower() == "yes":
    
  print("First name!")
  name = input("What is your name? ").capitalize().strip()
  if name not in list: 
    list.append(name)
  else:
    print("You are already in the list")
  print("Last name!")
  name = input("What is your name? ").capitalize().strip()
  if name not in list: 
    list.append(name)
  else:
    print("You are already in the list.")
  list_str = ' '.join(list)
  list_str += ","
  print(list_str)
  go = input("Would you like to add a person to the list?")
  
#other notes
#I called it "go" because I wanted to say "go again?" but you can't do that, so I abbreviated it!
