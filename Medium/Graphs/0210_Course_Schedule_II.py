"""
LeetCode 210 - Course Schedule II

Difficulty: Medium

Time Complexity: O(V + E)
Space Complexity: O(V + E)

Technique:
- Topological Sort (Kahn's Algorithm)
- BFS
"""

from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != numCourses:
            return []

        return order
