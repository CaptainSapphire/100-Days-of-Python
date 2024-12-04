print("Welcome my number list generator!")
print("The following numbers are going to determine what your list will start, end, and increment by.")
#SETUP
start = int(input("What is your starting number? "))
end = int(input("What is your ending number? "))
increment = int(input("What increment do you want to use?"))
#print("Start at: " + str(start))
#print("End before: " + str(start))
#print("Increment between values: " + str(increment))
## THE CODE
for i in range(start, end, increment):
  print(i)
