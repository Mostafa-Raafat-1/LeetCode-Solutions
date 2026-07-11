"""
LeetCode 217 - Contains Duplicate

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Hash Set
"""


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        for number in nums:
            if number in numbers:
                return True
            else:
                numbers.add(number) #amortized O(1)
        return False

# Time complexity = O(n)
# Space complexity = O(n)