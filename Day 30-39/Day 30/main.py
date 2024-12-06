##START
print("30 Days Down! Come share your thoughts with us on each :)")
for i in range (1, 30):
  thoughts = input("What do you think of day {count}? ".format(count=i))
  print(f"You thought day {i} was {thoughts}.")
