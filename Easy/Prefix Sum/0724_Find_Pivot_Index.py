"""
LeetCode 724 - Find Pivot Index

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Prefix Sum
- Running Sum
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)

        for i, number in enumerate(nums):
            right_sum = total_sum - left_sum - number
            if left_sum == right_sum:
                return i

            left_sum += number

        return -1
