# Reverse Prefix of Word (https://leetcode.com/problems/reverse-prefix-of-word/)
# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
# Complexity: O(n) time, O(n) space
# The second solution is more memory efficient in the sense, that it avoid concatenating 2 separate lists

# First solution using concatenating
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list = list(word)

        try:
            start_index = word_list.index(ch)
        except ValueError:
            return word

        reversed_part = word_list[:start_index+1][::-1]
        remaining_part = word_list[start_index+1:]
        word_list = reversed_part+remaining_part

        return ''.join(word_list)


# Second solution modifies list in place
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list = list(word)

        try:
            start_index = word_list.index(ch)
        except ValueError:
            return word

        word_list[:start_index+1] = word_list[:start_index+1][::-1]

        return ''.join(word_list)
