"""
LeetCode 27 - Remove Element

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Two Pointers
"""


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0

        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1

        return write
                

solution = Solution()
result = solution.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
print(result)