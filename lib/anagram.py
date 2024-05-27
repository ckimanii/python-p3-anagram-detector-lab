# your code goes here!

class Anagram:
    def __init__(self,word):
        self.word = word
    
    def match(self,word_list):
        matches = []

        for potential_anagram in word_list:
            if sorted(potential_anagram) == sorted(self.word) and potential_anagram!=self.word:
                matches.append(potential_anagram)
        return matches
