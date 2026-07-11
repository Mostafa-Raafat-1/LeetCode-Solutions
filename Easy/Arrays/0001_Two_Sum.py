"""
LeetCode 1 - Two Sum

Difficulty: Easy

Time Complexity: O(n²)
Space Complexity: O(1)
"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        loops = 0
        
        while True:
            if loops == len(nums) - 1:
                break
            
            elif nums[right] + nums[left] == target:
                return [left, right]
            elif left == right - 1:
                left +=1
                loops +=1
                right = len(nums) - 1
            else:
                right -=1
                    
solution = Solution()
result = solution.twoSum(nums = [3, 2, 4], target = 6)
print(result)