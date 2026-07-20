"""
LeetCode 383 - Ransom Note

Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(k)

Technique:
- Hash Map (Frequency Counting)
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(magazine)

        for char in ransomNote:
            if counts[char] == 0:
                return False
            counts[char] -= 1

        return True
