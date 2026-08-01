"""
LeetCode 4000 - Largest Integer With Given Digit Sum

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Greedy
- Math
"""


class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        number = 0
        remainder = s
        for i in range(n):
            if remainder <= 0:
                break
            digit = min(9, remainder)
            number += digit * 10 ** (n - i - 1)
            remainder -= digit
        return number if remainder == 0 else -1
