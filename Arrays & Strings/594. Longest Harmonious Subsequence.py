"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation:
The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2
Explanation:
The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:
Input: nums = [1,1,1,1]
Output: 0
Explanation:
No harmonic subsequence exists.
"""

"""
Find the largest subsequence in the array whose max and min value differ by 1.
We only need to return an integer of the max length subsequence.
We can remove some or no elements from the array.
Store a frequency of the elements in the list in a dict.
Iterate through the keys of the dict 
check if value+1 exists (ensures max and min differ by exactly 1)
if it does -> return freq[number] + freq[number+1]
"""
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freqs: dict[int] = {}
        max_subsequence: int = 0

        for number in nums:
            if number in freqs:
                freqs[number] += 1
            else:
                freqs[number] = 1
        
        for number in freqs:
            if number + 1 in freqs:
                curr_subsequence: int = freqs[number] + freqs[number+1]
                max_subsequence: int = max(max_subsequence, curr_subsequence)
        return max_subsequence

        