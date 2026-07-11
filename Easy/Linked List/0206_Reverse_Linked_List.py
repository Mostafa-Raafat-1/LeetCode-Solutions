"""
LeetCode 206 - Reverse Linked List

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Iterative
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        
        previous = head
        after = head.next
        head.next = None
        
        while after:
            current = after
            after = current.next
            current.next = previous
            previous = current
            
        head = previous
        
        return head

node5 = ListNode(val=5, next=None)
node4 = ListNode(val=4, next=node5)
node3 = ListNode(val=3, next=node4)
node2 = ListNode(val=2, next=node3)
node1 = ListNode(val=1, next=node2)
