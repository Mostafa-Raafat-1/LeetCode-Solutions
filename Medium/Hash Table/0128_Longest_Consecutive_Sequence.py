"""
LeetCode 128 - Longest Consecutive Sequence

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest_sequence = 0

        for number in numbers:
            if number - 1 not in numbers:
                current_sequence = 1

                while number + current_sequence in numbers:
                    current_sequence += 1

                longest_sequence = max(current_sequence, longest_sequence)

        return longest_sequence
