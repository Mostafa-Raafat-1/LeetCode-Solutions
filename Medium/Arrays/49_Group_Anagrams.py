"""
LeetCode 49 - Group Anagrams

Difficulty: Medium

Time Complexity: O(n * k)
Space Complexity: O(n * k)
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            counter_list = [0] * 26

            for char in string:
                counter_list[ord(char) - ord("a")] += 1

            counter_tuple = tuple(counter_list)
            anagrams[counter_tuple].append(string)

        return [element for element in anagrams.values()]
