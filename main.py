import random

# WordProvider  class for list getword action
class WordProvider:
    words = ["apple", "grape", "mango", "peach", "berry","lemon", "melon", "chili", "olive", "cocoa"]    
    def __init__(self):
        pass
    def get_word(self,):
        return random.choice(self.words)

class WordleGame:
    def __init__(self):
        # Set up the word provider and prepare storage for the secret word
        self.provider = WordProvider()
        self.secret = None

    def play_round(self):
        # Pick a random word and print it
        # Get and store a random word from the provider
        self.secret = self.provider.get_word()
        print("Secret word:", self.secret)
        while attempts < 6:
            guess = input("Enter your guess: ")
            if guess == self.secret:
                print("Correct! You guessed the word.")
                break
            else:
                 print("Wrong guess. Try again.")
            counter += 1


if __name__ == "__main__":
    game = WordleGame()
    game.play_round()
