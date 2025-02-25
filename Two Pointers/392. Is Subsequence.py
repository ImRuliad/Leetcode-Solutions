'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        define a pointer for s and a pointer for t
        traverse t via its pointer
        if t[pointer] == s[pointer] increment pointer for s.
        if pointer for s == len(s) return True
        if t is traversed return False
        '''
        if not s:
            return True

        ptr_s = 0
        for index in range(len(t)):
            if t[index] == s[ptr_s]:
                ptr_s += 1
            if ptr_s == len(s):
                return True
        return False