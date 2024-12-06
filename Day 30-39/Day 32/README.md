# Day 32

## Lesson Summary
Python uses lists instead of Arrays. Lists are literally lists of items. Any piece of data from any data type can go into a list. We can extract, remove, or change lists.
We can use a loop to move through data in a list without having to first manually tell the computer how many things are in that list.
We start counting the first item at 0 (instead of 1).
printing lists:
```

timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
print(timetable[1])
```
Changing lists go as such:
We built our list with timetable =, but we want to change index 4, "sport". We can do this by calling it with [ ].
```
timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4])

timetable[4]= "Watch TV"
print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4])
```
List loops: 
```
timetable = ["Computer Science", "Math", "English", "Art", "Watch TV"]
for lesson in timetable:
  print(lesson)
```
## Challenge Directions
Create a list that stores greetings in different languages. Start with the language you speak.
Then, go on the internet to find other greetings in other languages. Here is a list of greetings to get you started.
Import random library. Generate a random number between 0 and maximum number of items in your list.
At random, when the user clicks run, print one of the greetings.
Use an f-string.
