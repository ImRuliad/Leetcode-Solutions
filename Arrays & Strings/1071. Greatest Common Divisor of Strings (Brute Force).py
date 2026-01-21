"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str2 + str1 != str1 + str2:  
            return ""
        size1, size2 = len(str1), len(str2)

        for index, letter in reversed(list(enumerate(str2))):
            prefix = str2[:index+1]
            size_p = len(prefix)
            if size1 % size_p == 0 and size2 % size_p == 0:
                divisor1 = prefix * (size1 // size_p)
                divisor2 = prefix * (size2 // size_p)
                if divisor1 == str1 and divisor2 == str2:
                    return prefix

            