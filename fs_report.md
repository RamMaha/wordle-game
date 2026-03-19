This file is a merged representation of the entire codebase, combined into a single document

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block or partial content for large files

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

# Directory Structure
````
./
main.py
````

# Files

## File: main.py
````
import random

GREEN = "\033[92m"
GRAY  = "\033[90m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# WordProvider  class for list getword action
class WordProvider:
    def __init__(self):
        self.words = ["apple", "grape", "mango", "peach", "berry","lemon", "melon", "chili", "olive", "cocoa"]   
    def get_word(self,):
        return random.choice(self.words)

class WordleGame:
    def __init__(self):
        # Set up the word provider and prepare storage for the secret word
        self.provider = WordProvider()
        self.secret = None
        self.MAX_ATTEMPTS =6
        self.validator = GuessValidator()

    def play_round(self):
        # Pick a random word and print it
        # Get and store a random word from the provider
        self.secret = self.provider.get_word()
        print("Secret word:", self.secret)
        attempts =0
        while attempts < 6:
            guess = input("Enter your guess: ")
            feedback = self.validator.validate(guess, self.secret)
            print("".join(feedback))
            if guess == self.secret:
                print("Correct! You guessed the word.")
                break
            else:
                print("Wrong guess.")
                print("Attempts remaining:", self.MAX_ATTEMPTS - attempts)
            attempts += 1
        if(attempts == 6 and guess != self.secret):
            print("Out of attempts.")
            
class GuessValidator:
    def validate(self, guess, secret):
        feedback = [""] * len(secret)
        remaining_letters = list(secret)
        self._check_correct_positions(guess, remaining_letters, feedback)
        self._check_wrong_positions(guess, remaining_letters, feedback)
        return feedback

    def _check_correct_positions(self, guess, remaining_letters, feedback):
        for i in range(len(remaining_letters)):
            if guess[i] == remaining_letters[i]:
                feedback[i] = f"{GREEN}{guess[i]}{RESET}"
                remaining_letters[i] = None
            else: 
                feedback[i] = f"{GRAY}{guess[i]}{RESET}"
        return feedback

    def _check_wrong_positions(self, guess, remaining_letters, feedback):
        for i in range(len(guess)):
            # skip greens
            if feedback[i].startswith(GREEN):
                continue
            # if letter still available elsewhere
            raw_letter = guess[i]
            if raw_letter in remaining_letters:
                feedback[i] = f"{YELLOW}{raw_letter}{RESET}"
                # consume first unused occurrence
                remaining_letters[remaining_letters.index(raw_letter)] = None
            # else leave it gray



if __name__ == "__main__":
    game = WordleGame()
    game.play_round()
````
