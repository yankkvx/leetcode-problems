# Unique Morse Code Words (https://leetcode.com/problems/unique-morse-code-words/)
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# Return the number of different transformations among all words we have.
# Complexity: O(n * m) time(n is the number of words, m is the average length of the words), O(n) space (k - number of unique morse transformations. The set stores only unique transformations)


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        transformation = set()

        for word in words:
            morse_code = ''
            for char in word:
                index = ord(char) - ord('a')
                morse_code += morse[index]

            # Add transformation to the set(auto uniq)
            transformation.add(morse_code)

        return len(transformation)
