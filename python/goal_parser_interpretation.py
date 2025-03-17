# Goal Parser Interpretation (https://leetcode.com/problems/goal-parser-interpretation/)
# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
# The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
# Given the string command, return the Goal Parser's interpretation of command.
# Complexity: O(n) time, O(n) space

class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace('()', 'o')
        command = command.replace('(al)', 'al')
        return command
