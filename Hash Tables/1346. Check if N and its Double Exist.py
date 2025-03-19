"""
Given an array arr of integers, check if there exist two indices i and j such that :
    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        #declare a set to hold visited values
        #iterate through arr
        #check if curr_val * 2 in list is in arr:
        #   return the indices of curr_val and val in seen
        #add curr_val into seen.

        visited_numbers: set = set()

        for index, element in enumerate(arr):
            if (arr[index]*2) in visited_numbers or (arr[index]/2) in visited_numbers:
                return True
            visited_numbers.add(element)
        return False
