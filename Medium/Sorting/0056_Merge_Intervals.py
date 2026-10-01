"""
LeetCode 56 - Merge Intervals

Difficulty: Medium

Time Complexity: O(n log n)
Space Complexity: O(n)

Technique:
- Sorting
"""

# class Solution:
#     def merge(self, intervals: list[list[int]]) -> list[list[int]]:
#         intervals.sort(key=lambda x: x[0])

#         result = []

#         for interval in intervals:
#             if not result or result[-1][1] < interval[0]:
#                 result.append(interval)
#             else:
#                 result[-1][1] = max(result[-1][1], interval[1])

#         return result


"""
LeetCode 56 - Merge Intervals

Difficulty: Medium

Time Complexity: O(n log n)
Space Complexity: O(log n)

Technique:
- Quick Sort
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        def quick_sort(low, high):
            if low >= high:
                return

            i = low
            j = high
            pivot = intervals[(high + low) // 2][0]

            while j >= i:
                while intervals[i][0] < pivot:
                    i += 1

                while intervals[j][0] > pivot:
                    j -= 1

                if i <= j:
                    intervals[i], intervals[j] = intervals[j], intervals[i]
                    i += 1
                    j -= 1

            quick_sort(low, j)
            quick_sort(i, high)

        quick_sort(0, len(intervals) - 1)

        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
