# Minimum Sum of Four Digit Number After Splitting Digits (https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/)
# Given a four-digit integer `num`, split its digits into two new integers new1 and new2
# such that their sum is minimized. Leading zeros are allowed, and all digits must be used.
# The minimum sum can be achieved by sorting the digits and forming two numbers
# from alternating digits in sorted order.
# Complexity: O(1) time, O(1) space


class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted(str(num))
        first_number = int(nums[0] + nums[2])
        second_number = int(nums[1] + nums[3])

        return first_number + second_number
