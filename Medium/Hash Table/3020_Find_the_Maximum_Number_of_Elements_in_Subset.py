"""
LeetCode 3020 - Find the Maximum Number of Elements in Subset

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
from collections import Counter


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        longest_subset = 0

        if counts[1]:
            longest_subset = counts[1] if counts[1] % 2 else counts[1] - 1

        for number in counts:
            current_subset = 1
            if counts[number] >= 2 and number != 1:
                num_squared = number**2

                while counts[num_squared]:
                    current_subset += 2

                    if counts[num_squared] < 2:
                        break

                    num_squared **= 2

            longest_subset = max(longest_subset, current_subset)

        return longest_subset
