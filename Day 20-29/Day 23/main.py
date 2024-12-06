##Functions
def login(a, b):
  #10 attempts 
  for i in range(10):
    #asks for username and password
    user = input("What is your username?")
    passcode = input("What is your password?")
    if (a == user):
      if (b == passcode):
        print("Welcome to Replit!")
        break
    else: 
      print("Whoops! Your information is incorrect, invalid, or you are not registered. Try again!")
      

##
print("Replit Login System")
print("You have 10 login attempts.")

#a parameter
correct_username = "david"
#b parameter
correct_passcode = "beatlesyellowsubmarine"
#run the function/subroutine
login(correct_username, correct_passcode)
