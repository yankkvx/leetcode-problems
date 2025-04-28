# 1859. Sorting the Sentence (https://leetcode.com/problems/sorting-the-sentence/)
# Given a shuffled sentence with numbers attached to each word (1-indexed)
# return the original sentence with words in correct order without numbers
# Complexity: O(n log n) time, O(n) space

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        pairs = []

        for word in words:
            num = ''
            letters = ''
            for char in word:
                if char.isdigit():
                    num += char
                else:
                    letters += char
            pairs.append((int(num), letters))

        pairs.sort()
        result = [word for i, word in pairs]

        return ' '.join(result)
