"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
"""
#uses hashmap, not as intuitive, better solutions exist.
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        create a dict to track unique numbers.
        create a count variable to keep track of numbers in dict.
        sort nums.
        iterate through nums. 
        If element in nums not in dict -> dict[count] = element
        increment count by 1
        if count == 3, return dict[count]
        if count never reaches 3 return dict[1]
        """

        unique_nums: dict[int] = {}
        count = 1

        nums.sort(reverse=True)
        for element in nums:
            if element not in unique_nums.values():
                unique_nums[count] = element
                if count == 3:
                    return unique_nums[count]
                count += 1
        return unique_nums[1]