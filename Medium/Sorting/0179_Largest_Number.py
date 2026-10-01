from functools import cmp_to_key

"""
LeetCode 179 - Largest Number

Difficulty: Medium

Time Complexity: O(n log n * k)
Space Complexity: O(n)
"""


# class Solution:
#     def largestNumber(self, nums: list[int]) -> str:
#         nums = list(map(str, nums))

#         def compare(a, b):
#             if a + b > b + a:
#                 return -1
#             if a + b < b + a:
#                 return 1
#             return 0

#         nums.sort(key=cmp_to_key(compare))

#         if nums[0] == "0":
#             return "0"

#         return "".join(nums)


"""
LeetCode 179 - Largest Number

Difficulty: Medium

Time Complexity: O(n log n * k)
Space Complexity: O(n)

Technique:
- Merge Sort
"""


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def sort(low, high):
            if high - low < 1:
                return nums[low : high + 1]

            mid = (high + low) // 2
            left = sort(low, mid)
            right = sort(mid + 1, high)
            result = []

            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] + right[j] > right[j] + left[i]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        for i in range(len(nums)):
            nums[i] = str(nums[i])

        numbers = sort(0, len(nums) - 1)

        if numbers[0] == "0":
            return "0"

        result = ""
        for number in numbers:
            result += number

        return result
