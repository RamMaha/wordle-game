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
        attempts =0
        while attempts < self.MAX_ATTEMPTS:
            guess = input("Enter your guess: ")
            if not self.validator.is_valid(guess, self.secret):
                continue       # do not increment attempts
            attempts += 1  
            feedback = self.validator.validate(guess, self.secret)
            print("".join(feedback))
            if guess == self.secret:
                print("Correct! You guessed the word.")
                break
            else:
                print("Wrong guess.")
                print("Attempts remaining:", self.MAX_ATTEMPTS - attempts)
        if(attempts == 6 and guess != self.secret):
            print("Out of attempts.")
            
class GuessValidator:
    def validate(self, guess, secret):
        feedback = [""] * len(secret)
        remaining_letters = list(secret)
        self._check_correct_positions(guess, remaining_letters, feedback)
        self._check_wrong_positions(guess, remaining_letters, feedback)
        return feedback

    def is_valid(self, guess, secret):
        guess = guess.strip()
        if len(guess) != len(secret):
            print(f"Invalid guess length, expected {len(secret)} letters.")
            return False
        if not guess.isalpha():
            print("Guess must contain only letters.")
            return False
        return True
    
    def _check_correct_positions(self, guess, remaining_letters, feedback):
        for i in range(len(remaining_letters)):
            if guess[i] == remaining_letters[i]:
                feedback[i] = f"{GREEN}{guess[i]}{RESET}"
                remaining_letters[i] = None
            else: 
                feedback[i] = f"{GRAY}{guess[i]}{RESET}"
        return feedback

    def _check_wrong_positions(self, guess, remaining_letters, feedback):
        remaining_letters = list(remaining_letters)
        for i, letter in enumerate(guess):
            # skip already-colored (green) positions
            if feedback[i].startswith(GREEN):
                continue
            if letter in remaining_letters:
                feedback[i] = f"{YELLOW}{letter}{RESET}"
                # Consume that occurrence
                remaining_letters[remaining_letters.index(letter)] = None
                # else leave feedback[i] as the gray you set earlier
       
if __name__ == "__main__":
    game = WordleGame()
    game.play_round()
