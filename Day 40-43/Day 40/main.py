print("🌟Contact Card🌟")
name = input("Input your name > ")
birthday = input("Input your date of birth > ")
phone = input("Input your phone # > ")
email = input("Input your email > ")
address = input("Input your address > ")

user = {
    "name": name,
    "birthday": birthday,
    "phone": phone,
    "email": email,
    "address": address
}

print("Hello " + user["name"] + ". Our dictionary says that you were born on " + user["birthday"] + ", we can call you on " + user["phone"] + ", email " + user["email"] + ", or write to the " + user["address"] + ".")
