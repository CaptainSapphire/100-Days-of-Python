import time
print("STAR WARS NAME GENERATOR!!!⭐🛸🌌🌠")
time.sleep(1)
#Ask the user to input their first & last names.
first = input("What is your first name? ")
last = input("What is your last name? ")
#Slice the first 3 letters of the first name.
first3 = first[0:3]
#Slice the first 3 letters of the last name (surname).
last3 = last[0:3]
#Join them together. Ideally change the case so that it looks good - think fStrings or .upper()/.lower(). This is the user's Star Wars first name.
starwarsfirstname = (f"{first3.capitalize()}{last3.lower()}").capitalize()
#Now ask the user for their mother's maiden name and the city where they were born. (Maiden name is the last name they had before they got married. If you are not sure, make up a last name.)
maiden = input("What is your mother's maiden name? ")
city = input("What city were you born in? ")
#Combine the first two letters of the maiden name with the last 3 letters of the city to make the user's Star Wars last name. Remember, fStrings and .upper()/.lower().
maiden = maiden[0:2]
city = city[0:3]
starwarslastname = (f"{maiden.capitalize()}{city.lower()}").capitalize()
time.sleep(1)
#Finally, print them both as part of a sentence.
print("Congratulations! Your Star Wars name is " + starwarsfirstname + " " + starwarslastname)
