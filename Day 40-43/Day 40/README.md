# Day 40

## Lesson Summary
### Dictionaries
As you might have guessed, we love lists. However, list items are accessed in order by index number. This isn't always the way we want it to work.<br><br>

Dictionaries are a slightly different type of list that access data by giving each item a key. This creates what we call key:value pairs.<br><br>

Now we can access each item through its key, instead of having to remember what index it is at in the list.<br><br>

### Creating a dictionary - brace!
To create a dictionary we start just like a list, except with curly braces {}. This dictionary will store data about a user.
```
myUser = {"name": "David", "age": 128}
```
### Printing the keys
To output (print) from a dictionary, we can use the key instead of the index. Note that we still use square brackets for accessing items (ex: ["name"]).
```
myUser = {"name": "David", "age": 128}

print(myUser["name"])

# This code outputs 'David'.
```
### Changing an item
You can use the = syntax to change key values.
```
myUser = {"name": "David", "age": 128}

myUser["name"] = "The legendary David"
print(myUser)

# This code outputs 'name:'the legendary David', 'age':'128.
```

## Challenge Directions
Today's challenge is to create a contact card using a dictionary.<br><br>

1. Ask the user to input their name, date of birth, telephone number, email and physical address.
2. Store it all in a dictionary.
3. Print it out in a nice way once its stored.
Example:
```
🌟Contact Card🌟

Input your name > David Morgan

Input your date of birth > 01/01/1900

Input your telephone number > 01234 567890

Input your email > david@replit.com

Input your address > The Cupboard Under The Stairs, Replit Towers, NY.

Hi David Morgan. Our dictionary says that you were born on 01/01/1900, we can call you on 01234 567890, email david@replit.com, or write to The Cupboard Under The Stairs, Replit Towers, NY.
```
