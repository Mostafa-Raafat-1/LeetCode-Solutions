"""
LeetCode 169 - Majority Element

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
            
            
solution = Solution()
result = solution.majorityElement(nums = [1, 1, 1, 7, 2, 3, 3, 7, 7,7])
print(result)