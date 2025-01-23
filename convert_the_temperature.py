# Convert the Temperature (https://leetcode.com/problems/convert-the-temperature/)
# Given a temperature in Celsius, convert it to Kelvin and Fahrenheit. Return the results as an array
# Complexity: O(1) time, O(1) space


class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [round(kelvin, 5), round(fahrenheit, 5)]