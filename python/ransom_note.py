# Ransom Note (https://leetcode.com/problems/ransom-note/)
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Time complexity: O(n), where n is the length of the input strings. Space complexity: O(n). (we store character counts in dictionaries)

# First solution using Counter
from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # Count chars in ransomNote
        ransomNote_count = Counter(ransomNote)
        # Count chars in magazine
        magazine_count = Counter(magazine)

        for char in ransomNote_count:
            # If magazine lacks enough chars
            if ransomNote_count[char] > magazine_count.get(char, 0):
                return False
        return True


# Second solution using manual counting
class Solution(object):
    def canConstructAlt(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # Initialize dictionaries
        ransomNote_count = {}
        magazine_count = {}

        # Count characters in ransomNote
        for char in ransomNote:
            ransomNote_count[char] = ransomNote_count.get(char, 0) + 1

        # Count characters in magazine
        for char in magazine:
            magazine_count[char] = magazine_count.get(char, 0) + 1

        # Check if magazine has enough characters for ransomNote
        for char in ransomNote_count:
            if ransomNote_count[char] > magazine_count.get(char, 0):
                return False
        return True
