"""
LeetCode 382 - Linked List Random Node

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional
from random import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        current = self.head.next
        i = 2
        candidate = self.head.val

        while current:
            if random() < 1 / i:
                candidate = current.val

            current = current.next
            i += 1

        return candidate


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
