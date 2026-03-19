import random

# WordProvider  class for list getword action
class WordProvider:
    words = ["apple", "grape", "mango", "peach", "berry","lemon", "melon", "chili", "olive", "cocoa"]    
    def __init_(self):
        pass
    def get_word(self,):
        return random.choice(self.words)

WordProvider =  WordProvider()
print(WordProvider.get_word())