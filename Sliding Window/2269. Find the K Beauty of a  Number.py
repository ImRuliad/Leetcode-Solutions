"""
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:
    It has a length of k.
    It is a divisor of num.

Given integers num and k, return the k-beauty of num.
Note:
    Leading zeros are allowed.
    0 is not a divisor of any value.

A substring is a contiguous sequence of characters in a string.
"""

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        start: int = 0
        end: int = k
        str_num = str(num)
        count = 0

        while end <= len(str_num):
            int_num = int(str_num[start:end])
            if int_num >= 1:
                if num % int_num == 0:
                    count += 1
            start += 1
            end += 1
        return count
