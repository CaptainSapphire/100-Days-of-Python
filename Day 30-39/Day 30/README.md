# Day 30

## Lesson Summary
f-strings (format strings) are the best way to combine variables and text together. Change 1: Using {} as a placeholder for the variable. Change 2: Adding .format(variable names, commas). We can set local variables within the f-string itself. Now it doesn't matter the order of the variables.
```
name = "Katie"
age = "28"
pronouns = "she/her"

print("This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age))
```
Alighment:
left = <, right = >, center = ^

```
for i in range(1, 31):
  print(f"Day {i: <2} of 30")
```
## Challenge Directions
Create a program that uses a loop that asks the user what they have thought of each of the 30 days of challenges so far.

For each day, prompt the user to answer a question and restate it in a full sentence that is center aligned underneath the heading.
```
30 Days Down

Day 1: 
Amazing

            You thought Day 1 was amazing.
Day 2:
so good that I bought the David plushie

              You thought Day 2 was so good...
```
