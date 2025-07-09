"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left: int = 0
        right: int = 0
        max_consec: float = float('-INF')

        while right < len(nums):
            if nums[right] == 0:
                window_size: int = right - left
                max_consec = max(max_consec, window_size)
                left = right+1
            right += 1
        max_consec = max(max_consec, right-left)
        return max_consec