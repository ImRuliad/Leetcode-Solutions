"""
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left: int = 1
        right: int = num

        while left <= right:
            mid: int = left + (right-left) // 2
            square: int = mid*mid

            if square == num:
                return True
            if square > num:
                right = mid - 1
            if square < num:
                left = mid + 1
        return False