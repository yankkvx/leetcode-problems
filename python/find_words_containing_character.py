# Find Words Containing Character (https://leetcode.com/problems/find-words-containing-character/)
# Given an array of strings words and a character x, return an array of indices representing the words that contain the character x.
# Complexity: O(n*m) time (n - number of words, m - average word length), O(n) space

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for index, word in enumerate(words):
            if x in word:
                result.append(index)
        return result
