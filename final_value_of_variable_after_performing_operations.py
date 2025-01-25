# Final Value of Variable After Performing Operations (https://leetcode.com/problems/final-value-of-variable-after-performing-operations/)
# Given a list of operations that increment or decrement a variable X starting at 0, return its final value after performing all operations.
# Complexity: O(n) time, O(1) space

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if i == '--X' or i == 'X--':
                x -= 1
            else:
                x += 1
        return x
