"""
LeetCode 19 - Remove Nth Node From End of List

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Two Pointers
- Fast & Slow Pointers
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        previous = head
        current = head
        index = 0

        while current:
            if index < n + 1:
                current = current.next
                index += 1
                continue

            current = current.next
            previous = previous.next

        if previous == head and index < n + 1:
            return head.next
        previous.next = previous.next.next

        return head


# Chatgpt's Solution:
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode(0, head)
#         slow = dummy
#         fast = dummy

#         # Move fast n + 1 steps ahead.
#         for _ in range(n + 1):
#             fast = fast.next

#         # Move both pointers until fast reaches the end.
#         while fast:
#             slow = slow.next
#             fast = fast.next

#         # Remove the nth node from the end.
#         slow.next = slow.next.next

#         return dummy.next
