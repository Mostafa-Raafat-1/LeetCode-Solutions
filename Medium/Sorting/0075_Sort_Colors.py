"""
LeetCode 75 - Sort Colors

Difficulty: Medium

Time Complexity: O(n log n) average, O(n²) worst case
Space Complexity: O(log n) average, O(n) worst case

Technique:
- Quicksort
"""

# class Solution:
#     def sortColors(self, nums: list[int]) -> None:
#         def sort(low, high):
#             if low >= high:
#                 return

#             i = low
#             j = high
#             pivot = nums[(high + low) // 2]

#             while j >= i:
#                 while nums[i] < pivot:
#                     i += 1

#                 while nums[j] > pivot:
#                     j -= 1

#                 if j >= i:
#                     nums[j], nums[i] = nums[i], nums[j]
#                     i += 1
#                     j -= 1

#             sort(low, j)
#             sort(i, high)

#         sort(0, len(nums) - 1)


"""
LeetCode 75 - Sort Colors

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Three Pointers
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


Solution().sortColors([2, 0, 2, 0, 1, 0])
