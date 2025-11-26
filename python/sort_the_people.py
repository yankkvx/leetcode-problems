# 2418. Sort the People (https://leetcode.com/problems/sort-the-people/)
# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.
# Complexity: O(N log N) time, O(N) space


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = list(zip(heights, names))
        pairs.sort(reverse=True)
        result = []
        for height, name in pairs:
            result.append(name)
        return result
