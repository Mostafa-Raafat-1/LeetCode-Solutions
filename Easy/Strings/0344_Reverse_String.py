"""
LeetCode 344 - Reverse String

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Two Pointers
"""

"""---------------- Two Pointers ----------------"""
# from typing import List
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         left = 0
#         right = len(s) - 1

#         while right > left:
#             s[left], s[right] = s[right], s[left]
#             left +=1
#             right -=1


"""---------------- Recursion ----------------"""
"""
LeetCode 344 - Reverse String

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Recursion
- Two Pointers (Recursive)
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        def swap(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]

            swap(left + 1, right - 1)

        swap(0, len(s) - 1)
