"""
Given an integer array nums and an integer k.
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Find two unique indices whose elements are the same
        and the abs value of their difference is less than
        or equal to k.

        use a dict to keep track of duplicate elements.
        iterate through list using enumerate.
        add each element from list into dict -> key is element, val is index.
        if an element in list is in dict:
            compare the current index in list with key of matching element in dict.
            if less than or equal to k return true
        if entire list is traversed return false
        """

        visited: dict[int] = {}
        for index, element in enumerate(nums):
            if element in visited:
                if abs(index - visited[element]) <= k:
                    return True
            visited[element] = index
        return False