# your code goes here!

# lib/anagram.py

class Anagram:
    def __init__(self, word):
        # Store the base word in lowercase for consistent comparison
        self.word = word.lower()

    def match(self, word_list):
        # Sort the characters of the base word
        sorted_base_word = sorted(self.word)

        # Return all words that match the sorted base word
        return [word for word in word_list if sorted(word.lower()) == sorted_base_word]
