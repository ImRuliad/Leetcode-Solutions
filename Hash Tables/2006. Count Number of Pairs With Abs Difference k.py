'''
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
The value of |x| is defined as:
    x if x >= 0.
    -x if x < 0.

Example 1:
Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]

Example 2:
Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.

Example 3:
Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]
'''
from collections import Counter
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        '''
        get frequency of each num in nums, store in dict.
        for each num in nums -> if abs(nums[i]-k) in dict:
            counter += frequency of difference.
        '''

        occurrences = Counter(nums)
        count = 0

        for num in nums:
            smaller = num - k
            if smaller in occurrences:
                count += occurrences[smaller]
        return count
