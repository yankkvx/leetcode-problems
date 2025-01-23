# Score of a String (https://leetcode.com/problems/score-of-a-string/)
# Given a string s, the score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters. Return the score of s.
# Complexity: O(n) time (where n is the length of the input string), O(n) space (where n is the length of the input string)

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_list = list(s)
        ascii_list = []
        # Convert each char to ASCII value using ord()
        for i in char_list:
            ascii_code = ord(i)
            ascii_list.append(ascii_code)

        score = 0
        # Loop through the ASCII values and calculate the sum of abs differcences
        for i in range(1, len(ascii_list)):
            score += abs(ascii_list[i] - ascii_list[i-1])
        return score
