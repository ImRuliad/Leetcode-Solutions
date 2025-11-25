"""
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        max_ele = float('-inf')
        max_idx = 0
        size = len(arr)-1

        for idx, ele in enumerate(arr):
            max_ele = max(max_ele, ele)

        max_idx = arr.index(max_ele)
        if max_idx == 0 or max_idx == size:
            return False

        for index in range(max_idx):
            if arr[index] >= arr[index+1]:
                return False
        for index in range(max_idx, size):
            if arr[index] <= arr[index+1]:
                return False
        return True