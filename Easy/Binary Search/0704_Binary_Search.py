"""
LeetCode 704 - Binary Search

Difficulty: Easy

Time Complexity: O(log n)
Space Complexity: O(1)

Technique:
- Binary Search
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while high >= low:
            mid = (low + high) // 2
            middle=nums[mid]
            if middle == target:
                return mid
            elif middle > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
solution = Solution()
result = solution.search(nums=[1,3], target=3)
print(result)