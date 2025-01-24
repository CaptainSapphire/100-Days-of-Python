# doictionary
#name url desc star rating of 5
#loop to names
print("🌟Website Rating🌟")
name = input("Input your website name: ")
url = input("Input your url: ")
desc = input("Input your description: ")
rating = input("Input your star rating out of 5: ")

website = {"name" : name, "url": url, "desc": desc, "rating": rating}

for name, value in website.items():
  print(name + ": " + value)
