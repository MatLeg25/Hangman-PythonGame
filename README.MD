# Hangman

Python command line game.

![hangman](https://user-images.githubusercontent.com/70913892/133148187-8bdb6138-9bba-418e-b228-f48d91f9eaf3.PNG)


## Game logic:
- The function uses its parameter `word` as the word to guess and `lives` to as the number of available mistakes
- The initial game state is displayed as `_ _ _ _ _ _ _ _` (one underscore for each letter in `word`)
- The game state is displayed as `_ o d _ _ o o _` if letters 'd' and 'o' have been revealed
- It is possible to make guesses, and letters that occur in the word are revealed
- When a guessed letter does not occur in `word`, the player loses one life
- When a guess is repeated (regardless of its occurrences), the player is notified, and nothing happens
- When a guess is wrong (either a new or a repeated letter), the already tried missing letters are shown to the user
- The player wins when all the letters in `word` have been revealed
- The player loses when misses a letter for the `lives`th time (not counting repeated guesses)
- When the player types `'quit'` as input, the program says good-bye and terminates
