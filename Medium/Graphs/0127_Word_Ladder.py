"""
LeetCode 127 - Word Ladder

Difficulty: Hard

# N: Number of words in wordList, L: Length of each word
Time Complexity: O(N * L²)
Space Complexity: O(N)

Technique:
- Breadth-First Search (BFS)
"""

from typing import List
from collections import deque


class Solution:
    def _get_neighbors(self, word):
        for i in range(len(word)):
            for char_code in range(ord("a"), ord("z") + 1):
                character = chr(char_code)

                if character == word[i]:
                    continue

                yield word[:i] + character + word[i + 1 :]

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        visited = {beginWord}
        queue = deque([beginWord])
        level = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                for neighbor in self._get_neighbors(word):
                    if neighbor == endWord:
                        return level + 1

                    if neighbor in words and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            level += 1

        return 0
