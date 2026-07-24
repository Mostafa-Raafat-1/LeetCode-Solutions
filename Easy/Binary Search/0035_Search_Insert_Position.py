"""
LeetCode 35 - Search Insert Position

Difficulty: Easy

Time Complexity: O(log n)
Space Complexity: O(1)

Technique:
- Binary Search
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while high >= low:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return low
