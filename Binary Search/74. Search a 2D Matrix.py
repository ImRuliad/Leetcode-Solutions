"""
You are given an m x n integer matrix matrix with the following two properties:
    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        start = 0
        end = (rows * cols) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if matrix[mid // cols][mid % cols] > target:
                end = mid - 1
            elif matrix[mid // cols][mid % cols] < target:
                start = mid + 1
            else:
                return True
        return False