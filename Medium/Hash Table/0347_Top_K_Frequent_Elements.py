"""
LeetCode 347 - Top K Frequent Elements

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        for num, freq in count.items():
            buckets[freq].append(num)

        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)

            if len(result) == k:
                return result

        return result
