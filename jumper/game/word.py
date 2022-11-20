import random

class Word:

    def __init__(self):
        
        self.words = ["Chocolate", "Strawberry", "Apple", "Pineapple", "Coconut"]
        self.value = random.choice(self.words)
        self.hidden_word = len(self.value) * "_"

    def reveal_letter(self, letter):

        for i in range(len(self.value)):
            if letter.lower() == self.value[i].lower():
                if letter == self.value[0]:
                    self.hidden_word = letter.upper() + self.hidden_word[i+1:]
                else:
                    self.hidden_word = self.hidden_word[:i] + letter + self.hidden_word[i+1:]