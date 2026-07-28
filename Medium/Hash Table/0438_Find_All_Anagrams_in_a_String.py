"""
LeetCode 438 - Find All Anagrams in a String

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)
# (O(26) auxiliary space since the alphabet is fixed, or O(k) where k is the
# number of distinct characters if considering a general character set.)

Technique:
- Sliding Window
- Hash Table (Counter)
"""

from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window_count = Counter(s[: len(p)])

        result = []

        if window_count == p_count:
            result.append(0)

        for i in range(len(p), len(s)):
            window_count[s[i]] += 1

            left_char = s[i - len(p)]
            window_count[left_char] -= 1

            if window_count[left_char] == 0:
                del window_count[left_char]

            if window_count == p_count:
                result.append(i - len(p) + 1)

        return result
