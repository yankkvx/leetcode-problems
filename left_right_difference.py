# Left and Right Sum Differences (https://leetcode.com/problems/left-and-right-sum-differences/)
# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
# - answer[i] = |leftSum[i] - rightSum[i]|
# - leftSum[i] is the sum of elements to the left of index i in the array nums
# - rightSum[i] is the sum of elements to the right of index i in the array nums
# Complexity: O(n) time, O(n) space

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_sum = [0] * n
        right_sum = [0] * n
        answer = [0] * n

        for i in range(1, n):
            left_sum[i] = left_sum[i-1] + nums[i-1]

        # Iterate through the array in reverse order,  starting from index n-2 and stopping at index 0
        for i in range(n-2, -1, -1):
            right_sum[i] = right_sum[i+1] + nums[i+1]

        # Calculate the absolute difference between left and right sums
        for i in range(n):
            answer[i] = abs(left_sum[i] - right_sum[i])

        return answer
