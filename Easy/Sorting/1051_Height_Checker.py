"""
LeetCode 1051 - Height Checker

Difficulty: Easy

Time Complexity: O(n + k)
Space Complexity: O(k)

Technique:
- Counting Sort
"""


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        k = 101
        counts = [0] * k
        index = 0
        result = 0

        for height in heights:
            counts[height] += 1

        for height, count in enumerate(counts):
            for _ in range(count):
                if heights[index] != height:
                    result += 1
                index += 1

        return result
