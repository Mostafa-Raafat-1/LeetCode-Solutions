"""
LeetCode 148 - Sort List

Difficulty: Medium

Time Complexity: O(n log n)
Space Complexity: O(log n)

Technique:
- Divide and Conquer
- Merge Sort
- Slow/Fast Pointers
"""

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def sortList(self, head: ListNode | None) -> ListNode | None:
#         if not head:
#             return None
#         if not head.next:
#             return head

#         fast = slow = head
#         prev = None
#         while fast and fast.next:
#             prev = slow
#             slow = slow.next
#             fast = fast.next.next

#         right = self.sortList(slow)
#         prev.next = None
#         left = self.sortList(head)

#         dummy = ListNode()
#         current = dummy

#         while left and right:
#             if right.val < left.val:
#                 current.next = right
#                 right = right.next
#             else:
#                 current.next = left
#                 left = left.next

#             current = current.next

#         current.next = left if left else right
#         return dummy.next


"""
LeetCode 148 - Sort List

Difficulty: Medium

Time Complexity: O(n log n)
Space Complexity: O(1)

Technique:
- Bottom-Up Merge Sort
- Iterative
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        dummy = ListNode(0)
        dummy.next = head

        size = 1

        while size < length:
            prev = dummy
            current = dummy.next

            while current:
                left = current
                right = self.split(left, size)

                current = self.split(right, size)

                merged = self.merge(left, right)

                prev.next = merged

                while prev.next:
                    prev = prev.next

            size *= 2

        return dummy.next

    def split(self, head, size):
        if not head:
            return None

        current = head

        for _ in range(size - 1):
            if not current.next:
                break
            current = current.next

        next_head = current.next
        current.next = None

        return next_head

    def merge(self, left, right):
        dummy = ListNode()
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        current.next = left if left else right

        return dummy.next


head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
Solution().sortList(head)
