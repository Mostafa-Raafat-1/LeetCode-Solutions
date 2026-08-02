"""
LeetCode 560 - Subarray Sum Equals K

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Prefix Sum
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        seen = {0: 1}
        result = 0

        for i, number in enumerate(nums):
            new_sum = number + total
            target = new_sum - k
            if target in seen:
                result += seen[target]

            seen[new_sum] = seen.get(new_sum, 0) + 1
            total = new_sum

        return result


print(Solution().subarraySum(nums=[1, 1, 1], k=2))
