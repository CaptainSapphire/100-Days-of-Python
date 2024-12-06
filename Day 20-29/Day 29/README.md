# Day 29

## Lesson Summary
Add a space between each number with end=" ".
```
for i in range(0, 100):
  print(i, end=" ")
```
More:
```
#new line
for i in range(0, 100):
  print(i, end="\n")
#tab indent
for i in range(0, 100):
  print(i, end="\t")
#vertical tab
for i in range(0, 100):
  print(i, end="\v")
```
sep (separator)
```
print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")
```
The ability to turn off the cursor:
```
import os, time
print('\033[?25l', end="")
for i in range(1, 101):
  print(i)
  time.sleep(0.2)
  os.system("clear")
```
## Challenge Directions
Write a subroutine that writes text in color. All it will do is print out the text in that color and turn the color back to normal when it's finished.

Control end and sep so there are not random symbols or spaces.

Check out this github resource for the color codes.
