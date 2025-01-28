# Truncate Sentence (https://leetcode.com/problems/truncate-sentence/)
# Given a sentence s and an integer k, you need to truncate the sentence such thatit contains only the first k words. Return the truncated sentence.
# Complexity: O(n) time, O(n) space


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s_list = s.split()
        s_list = s_list[:k]
        return ' '.join(s_list)
