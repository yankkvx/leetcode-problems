# 1281. Subtract the Product and Sum of Digits of an Integer (https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)
# Given an integer number n, return the difference between the product of its digits and the sum of its digits
# Complexity: O(n) time, O(1) space


# Using list manipulation
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        new_list = [int(digit) for digit in str(n)]
        product_of_digits = 1

        for num in new_list:
            product_of_digits *= num

        return product_of_digits - sum(new_list)


# Using direct number manipulation
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_of_digits = 1
        sum_of_digits = 0

        while n > 0:
            digit = n % 10
            product_of_digits *= digit
            sum_of_digits += digit
            n //= 10

        return product_of_digits - sum_of_digits
