# 2114. Maximum Number of Words Found in Sentences (https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/)
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces
# You are given an array of strings sentences, where each sentences[i] represents a single sentence
# Return the maximum number of words that appear in a single sentence
# Complexity: O(n) time, O(1) space


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sentence.split()) for sentence in sentences)


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        new_list = []
        for sentence in sentences:
            word_count = len(sentence.split())
            new_list.append(word_count)
        return max(new_list)
