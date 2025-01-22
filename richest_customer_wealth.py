# Richest Customer Wealth (https://leetcode.com/problems/richest-customer-wealth/)
# Given an m x n integer grid accounts, where accounts[i][j] represents the amount of money the i customer has in the j bank.
# A customers wealth is the sum of money in all their bank accounts. Return the wealth of the richest customer.
# Complexity: O(m*n) time, O(1) space (only 1 variable is used).

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_bank = 0
        for customer in accounts:
            bank = sum(customer)
            if bank > max_bank:
                max_bank = bank
        return max_bank
