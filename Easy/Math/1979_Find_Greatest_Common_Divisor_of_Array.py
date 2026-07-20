"""
LeetCode 1979 - Find Greatest Common Divisor of Array

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Euclidean Algorithm
"""


from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)

        while b:
            a, b = b, a % b

        return a