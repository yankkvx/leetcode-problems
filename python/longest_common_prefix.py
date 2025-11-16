# Longest Common Prefix (https://leetcode.com/problems/longest-common-prefix/)
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Complexity: O(N*Log(N)) time, O(n) space


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i+=1

        return first[:i]

