"""
LeetCode 684 - Redundant Connection

Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(n)

Technique:
- DFS
"""

from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def has_path(vertex, target, parent, visited):
            if vertex == target:
                return True

            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor == parent:
                    continue

                if neighbor not in visited:
                    if has_path(neighbor, target, vertex, visited):
                        return True

            return False

        for vertex1, vertex2 in edges:
            visited = set()

            if has_path(vertex1, vertex2, None, visited):
                return [vertex1, vertex2]

            graph[vertex1].append(vertex2)
            graph[vertex2].append(vertex1)
