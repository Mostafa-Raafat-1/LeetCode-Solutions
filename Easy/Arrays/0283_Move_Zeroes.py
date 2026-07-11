"""
LeetCode 283 - Move Zeroes

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Two Pointers
"""


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
        
solution = Solution()
result = solution.moveZeroes([0,1,0,3,12])