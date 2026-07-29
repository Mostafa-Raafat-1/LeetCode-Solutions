"""
LeetCode 219 - Contains Duplicate II

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for i, number in enumerate(nums):
            if number in last_seen and i - last_seen[number] <= k:
                return True

            last_seen[number] = i

        return False
