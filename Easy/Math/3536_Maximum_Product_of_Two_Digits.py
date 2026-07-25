"""
LeetCode 3536 - Maximum Product of Two Digits

Difficulty: Easy

Time Complexity: O(d) (Number of Digits)
Space Complexity: O(1)
"""


class Solution:
    def maxProduct(self, n: int) -> int:
        largest = 0
        second_largest = 0
        new_number = n

        while new_number > 0:
            remainder = new_number % 10
            new_number //= 10

            if remainder >= largest:
                second_largest = largest
                largest = remainder
            elif remainder > second_largest:
                second_largest = remainder

        return largest * second_largest
