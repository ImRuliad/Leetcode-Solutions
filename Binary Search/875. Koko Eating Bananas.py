"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        import math

        left: int = 1  # smallest amount of bananas eaten per hour.
        right: int = max(piles)  # largest amount of bananas eaten per hour.

        while left < right:
            # the middle of smallest and largest bananas per hour.
            mid: int = left + (right - left) // 2
            total_hours = 0

            for amt_banana in piles:
                total_hours += math.ceil(amt_banana / mid)

            if total_hours > h:
                left = mid + 1
            if total_hours <= h:
                right = mid

        return left
