"""
LeetCode 303 - Range Sum Query - Immutable

Difficulty: Easy

Time Complexity:
- __init__: O(n)
- sumRange: O(1)

Space Complexity: O(n)

Technique:
- Prefix Sum
"""

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]

        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
