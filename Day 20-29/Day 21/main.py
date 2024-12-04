print("Math Game!")
print("Do you know your math times tables? ")
multiple = input("Name your multiple: ")
score = 0
multiplyby = 1
##the main part
for i in range(1, 11):
  print(i)
  #check if their answer is correct
  if int(input(f"{i} X {multiple} = ")) == i * int(multiple):
    print("Awesome!")
    score = score + 1
  else:
    print("Nope. Answer was", i * int(multiple))

print("----")
print("You scored " + str(score) + " out of 10.")

