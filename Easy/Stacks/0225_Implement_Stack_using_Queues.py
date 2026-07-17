"""
LeetCode 225 - Implement Stack using Queues

Difficulty: Easy

Time Complexity:
- push()  : O(n)
- pop()   : O(1)
- top()   : O(1)
- empty() : O(1)

Space Complexity: O(n)
"""


from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q