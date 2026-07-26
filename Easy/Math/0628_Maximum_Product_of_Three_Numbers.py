"""
LeetCode 628 - Maximum Product of Three Numbers

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest = second_largest = third_largest = float("-inf")
        smallest = second_smallest = float("inf")

        for number in nums:
            if number <= smallest:
                second_smallest = smallest
                smallest = number
            elif number < second_smallest:
                second_smallest = number

            if number >= largest:
                third_largest = second_largest
                second_largest = largest
                largest = number
            elif number >= second_largest:
                third_largest = second_largest
                second_largest = number
            elif number > third_largest:
                third_largest = number

        largest_products = largest * second_largest * third_largest
        largest_smallest_products = largest * smallest * second_smallest
        return max(largest_products, largest_smallest_products)


print(Solution().maximumProduct([-10, -10, 5, 2]))
