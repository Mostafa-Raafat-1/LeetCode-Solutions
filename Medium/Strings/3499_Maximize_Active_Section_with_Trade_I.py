"""
LeetCode 3499 - Maximize Active Section with Trade I

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"

        segments = []
        current = t[0]
        length = 1

        for char in t[1:]:
            if char == current:
                length += 1
            else:
                segments.append((current, length))
                current = char
                length = 1

        segments.append((current, length))

        max_gain = 0

        for i in range(1, len(segments) - 1):
            if segments[i][0] == '1':
                gain = segments[i - 1][1] + segments[i + 1][1]
                max_gain = max(max_gain, gain)

        return s.count('1') + max_gain