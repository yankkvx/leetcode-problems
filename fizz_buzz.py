# Fizz Buzz (https://leetcode.com/problems/fizz-buzz/)
# Given an integer n, return a string array where:
# - answer[i] == "FizzBuzz" if i is divisible by 3 and 5
# - answer[i] == "Fizz" if i is divisible by 3
# - answer[i] == "Buzz" if i is divisible by 5
# - answer[i] == i (as a string)
# Complexity: O(n) time, O(n) space (new list is created).

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        new_list = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                new_list.append('FizzBuzz')
            elif i % 5 == 0:
                new_list.append('Buzz')
            elif i % 3 == 0:
                new_list.append('Fizz')
            else:
                new_list.append(str(i))
        return new_list
