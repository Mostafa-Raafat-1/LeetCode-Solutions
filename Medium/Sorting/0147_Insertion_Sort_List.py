"""
LeetCode 147 - Insertion Sort List

Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(1)

Technique:
- Insertion Sort
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        dummy = ListNode(0, head)
        prev = head
        current = head.next

        while current:
            # Current node is already in the correct position.
            if current.val >= prev.val:
                prev = current
                current = current.next
                continue

            next_node = current.next

            # Find the node immediately before current's new position.
            pointer = dummy
            while pointer.next.val <= current.val:
                pointer = pointer.next

            # Remove current from its old position.
            prev.next = next_node

            # Insert current into its new position.
            current.next = pointer.next
            pointer.next = current

            current = next_node

        return dummy.next
