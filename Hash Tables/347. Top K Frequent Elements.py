"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        freq = {}
        heap = []
        ordered_numbers = []

        for number in nums:
            if number in freq:
                freq[number] += 1
            else:
                freq[number] = 1

        for key,value in freq.items():
            heapq.heappush(heap, (-value, key))
        
        for _ in range(k):
            ordered_numbers.append(heapq.heappop(heap)[1])
        return ordered_numbers