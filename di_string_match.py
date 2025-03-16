# 942. DI String Match (https://leetcode.com/problems/di-string-match/)
# Reconstruct the permutation perm from the given string s where I indicates
# the current element is smaller than the next and D indicates its larger
# Complexity: O(n) time, O(n) space


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        len_s = len(s)
        low, high = 0, len_s
        result = []

        for i in s:
            if i == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        result.append(low)
        return result
