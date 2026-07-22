"""
LeetCode 238 - Product of Array Except Self

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)
(Note: The output array is not counted as extra space.)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        suffix = 1

        for i in range(1, len(nums)):
            left.append(left[i - 1] * nums[i - 1])

        for i in range(len(nums) - 1, -1, -1):
            left[i] *= suffix
            suffix *= nums[i]

        return left
