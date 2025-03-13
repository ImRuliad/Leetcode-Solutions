"""
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
Return any answer array that satisfies this condition.

Example 1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:
Input: nums = [2,3]
Output: [2,3]
"""


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
        Create a new array with same length as nums
        use two pointers even and odd to keep track of even indices and odd indices.
        even starts at 0, odd starts at 1
        iterate through nums to get each element
        if element is even -> new_list[even] = element -> even += 2
        if element in odd -> new_list[odd] = element -> odd += 2
        """

        sorted_list = [0] * len(nums)

        even: int = 0
        odd: int = 1

        for number in nums:
            if number % 2 == 0:
                sorted_list[even] = number
                even += 2
            if number % 2 != 0:
                sorted_list[odd] = number
                odd += 2
        return sorted_list


