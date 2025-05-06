'''
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

Example 1:
Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.

Example 2:
Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]
Explanation: The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.

Example 3:
Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
Explanation: No value is present in at least two arrays.
'''

from itertools import zip_longest
from collections import defaultdict


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        occurences = defaultdict(int)
        distinct_list = []

        set1, set2, set3 = set(nums1), set(nums2), set(nums3)

        for (num1, num2, num3) in zip_longest(set1, set2, set3):
            occurences[num1] += 1
            occurences[num2] += 1
            occurences[num3] += 1

        for number in occurences:
            if occurences[number] >= 2 and number is not None:
                distinct_list.append(number)

        return distinct_list
