# Convert Date to Binary (https://leetcode.com/problems/convert-date-to-binary/)
# You are given a string date in the yyyy-mm-dd format return the binary representation of date.
# Complexity: O(1) time, O(1) memory


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split('-')
        return f"{format(int(year), 'b')}-{format(int(month), 'b')}-{format(int(day), 'b')}"
