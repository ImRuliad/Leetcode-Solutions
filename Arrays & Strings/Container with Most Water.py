"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        left ptr = 0 right ptr = len(height)-1

        while left < right
            curr_volume = min(height[left], height[right]) * (right-left)
            max_vol = max(max_vol, curr_volume)

            if height[left] < height[right] then left += 1
            if height[right] < height[left] then right -= 1
            if height[left] == height[right] then left += 1
        """

        left, right = 0, len(height) - 1
        max_vol = 0

        while left < right:
            curr_vol = min(height[left], height[right]) * (right - left)
            max_vol = max(max_vol, curr_vol)

            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return max_vol