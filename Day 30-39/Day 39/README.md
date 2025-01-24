# Day 39
## Lesson Summary
👉 random.choice() picks a random item from a list.

Here's a list of words:
```
listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]
```
To select randomly from this list, we assign random.choice() to a variable. We give random.choice() the name of the list in the brackets.
```
listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]
wordChosen = random.choice(listOfWords)
```
There's lots of other stuff needed to make this program work, but, we'll break that down in the challenge section of today's tutorial.

## Challenge Directions
Once the word has been picked, the following things need to happen:<br><Br>

- Prompt the user to type in a letter.
- Check if the letter is in the word.
- If it does, output the word with all blanks apart from the letter(s) they've already guessed.
- Keep a running list of the letters they've used.
- Count how many times they've picked a letter that isn't in the word - more than 6 and they lose.
- Output a 'win' message if they reveal all the letters.
- 🥳 Extra points for using ASCII art to draw the hangman as the player makes incorrect guesses.

Example:
```
🌟Hangman🌟

Choose a letter: i
Nope, not in there.
5 left.

Choose a letter: a
Correct!
__a__

Choose a letter: s
Correct!
s_a__

Choose a letter: u
Correct!
sua__

# Repeat until.....
# If user wins
You won with 5 lives left.

# Loses
You lost!
```
