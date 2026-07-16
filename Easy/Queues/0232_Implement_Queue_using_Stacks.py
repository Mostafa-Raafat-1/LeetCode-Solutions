"""
LeetCode 232 - Implement Queue using Stacks

Difficulty: Easy

Time Complexity:
- push()  : O(1)
- pop()   : Amortized O(1)
- peek()  : Amortized O(1)
- empty() : O(1)

Space Complexity: O(n)

Technique:
- Two Stacks
- Amortized Analysis
"""


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def _transfer(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
    def pop(self) -> int:
        if not self.stack2:
            self._transfer()

        return self.stack2.pop()
        

    def peek(self) -> int:
        if not self.stack2:
            self._transfer()
        
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2