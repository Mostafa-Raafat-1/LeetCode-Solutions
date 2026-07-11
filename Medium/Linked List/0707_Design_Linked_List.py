"""
LeetCode 707 - Design Linked List

Difficulty: Medium

Time Complexity:
- get: O(n)
- addAtHead: O(1)
- addAtTail: O(n)
- addAtIndex: O(n)
- deleteAtIndex: O(n)

Space Complexity: O(1)

Technique:
- Singly Linked List
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        
        if current is None:
            return -1
        
        i = 0
        while True:
            if i == index:
                return current.val
            
            if current.next:
                current = current.next
                i +=1
            else:
                return -1
        

    def addAtHead(self, val: int) -> None:
        node = Node(val=val)
        
        node.next = self.head
        self.head = node
        

    def addAtTail(self, val: int) -> None:
        node = Node(val=val)

        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        current = self.head
        i = 0

        while current and i < index - 1:
            current = current.next
            i += 1

        if current is None:
            return

        node = Node(val)
        node.next = current.next
        current.next = node
        

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        previous = self.head
        i = 0

        while previous and i < index - 1:
            previous = previous.next
            i += 1

        if previous is None or previous.next is None:
            return

        previous.next = previous.next.next