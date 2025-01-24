# Day 37

## Lesson Summary
string splicing = chopping a string into chunks or taking portions out. <br><br>
To slice a single character from a string, you use the index of that character in square brackets [] just like you'd use with a list.<br><br>
To slice more than one character, you use two indices (yes that is the plural form of 'index'): the start character and one after your desired end character.<br><br>
👉 Leaving the first index blank defaults to 'start from index 0'.<br>
👉 Leaving the last index blank defaults to 'go to the end'.<br><br>
Adding a third argument to the square brackets [] specifies the gap left between characters.<br><br>
Using a negative number in the third argument can be super useful. It starts the slice from the end of the string instead of the beginning.<br><br>
👉 split lets us split a string into a list of individual words by separating it at the space characters.<br><br>

## Challenge Directions
This is the challenge you're looking for. This program will generate your Star Wars Name.<br><br>

- Ask the user to input their first & last names.
- Slice the first 3 letters of the first name.
- Slice the first 3 letters of the last name (surname).
- Join them together. Ideally change the case so that it looks good - think fStrings or .upper()/.lower(). This is the user's Star Wars first name.
- Now ask the user for their mother's maiden name and the city where they were born. (Maiden name is the last name they had before they got married. If you are not sure, make up a last name.)
- Combine the first two letters of the maiden name with the last 3 letters of the city to make the user's Star Wars last name. Remember, fStrings and .upper()/.lower().
- Finally, print them both as part of a sentence.
- 🥳 Extra points for getting all the inputs with just one input command and the split function.

Example:
```
🌟Star Wars Name Generator🌟

Input your first name > David

Input your lastname > Morgan

Input your mother's maiden name > Jones

Input the city where you were born > Cardiff

Your Star Wars name is Davmor Joiff
```
