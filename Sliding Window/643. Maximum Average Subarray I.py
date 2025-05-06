"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000

Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
"""
6
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        window_start: int = 0
        window_end: int = k
        size_of_nums: int = len(nums)
        max_avg: float = float('-inf')
        element_sum: float = 0
        element_avg: float = 0

        for element in nums[window_start:window_end]:
            element_sum += element

        while window_end < size_of_nums:
            element_avg: float = element_sum / k
            max_avg: float = max(max_avg, element_avg)

            element_sum -= nums[window_start]
            element_sum += nums[window_end]
            window_start += 1
            window_end += 1

        element_avg: float = element_sum / k
        max_avg: float = max(max_avg, element_avg)

        return max_avg