# your code goes here!
#!/usr/bin/env python3

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, candidates):
        # Normalize the reference word by sorting its letters
        sorted_ref = sorted(self.word)
        matches = [
            candidate
            for candidate in candidates
            if sorted(candidate) == sorted_ref
        ]
        return matches
