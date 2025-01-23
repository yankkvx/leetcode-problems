# Minimum Number Game (https://leetcode.com/problems/minimum-number-game/)
# Create a new list by iteratively removing the two smallest numbers from the original list and appending them in reverse order until all numbers are processed.
# The second and third variants the mist sutable for most cases, but i prefer the third for its cleaner syntax using an iterator.
# But if we need to minimaze additional memory usage the variant with bubble sort is the best choice, cause the sorting is done in-place and requires O(1) space.

# Complexity: O(n^2) time, O(n) space. The least efficient, cause it's needs the same time, as bubble sort while using more memory
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        result = []
        while nums:
            alice_pick = min(nums)
            nums.remove(alice_pick)
            if nums:
                bob_pick = min(nums)
                nums.remove(bob_pick)
                result.extend([bob_pick, alice_pick])
            else:
                result.append(alice_pick)
        return result


# Sorting the array and processing in pairs. Complexity: O(n log n) time, O(n) space
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()
        for i in range(0, len(nums), 2):
            result.append(nums[i+1])
            result.append(nums[i])
        return result


# Using iterator. Complexity: O(n log n) time, O(n) space.
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        iterator = iter(nums)
        for i, j in zip(iterator, iterator):
            result.append(j)
            result.append(i)
        return result


# Using bubble sort. Complexity: O(n^2) time, O(1) space. The best choice to minimize additional memory usage
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break

        for i in range(1, n, 2):
            nums[i-1], nums[i] = nums[i], nums[i-1]
        return nums
