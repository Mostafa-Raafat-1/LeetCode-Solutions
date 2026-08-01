"""
LeetCode 4006 - Count Valid Prefixes

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def countValidPrefixes(self, s: str) -> int:
        counter = {"0": 0, "1": 0}
        total = 0

        for number in s:
            counter[number] += 1
            zero_counter = counter["0"]
            one_counter = counter["1"]

            if abs(zero_counter - one_counter) <= 1:
                total += 1

        return total
