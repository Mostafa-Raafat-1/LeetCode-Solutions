"""
LeetCode 207 - Course Schedule

Difficulty: Medium

Time Complexity: O(V + E)
Space Complexity: O(V + E)

Technique:
- DFS
"""

from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        gray = set()
        black = set()

        def detect_cycle(vertex):
            gray.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor in gray:
                    return True
                if neighbor in black:
                    continue

                if detect_cycle(neighbor):
                    return True

            gray.remove(vertex)
            black.add(vertex)
            return False

        for vertex in range(numCourses):
            if vertex not in black and detect_cycle(vertex):
                return False
        return True
