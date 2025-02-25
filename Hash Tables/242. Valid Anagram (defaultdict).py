'''
Given two strings s and t, return true if t is an of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # iterate through string "s" using enumeration
        # if a letter in "s" is present in list "t" then pop the letter in list "t"
        # if a lettter in "s" is NOT present in list "t" then return false
        # once done iterating through string "s" return true

        if len(s) != len(t):
            return False

        dict_for_s = defaultdict(int)
        dict_for_t = defaultdict(int)

        for index, element in enumerate(s):
            dict_for_s[element] += 1
            dict_for_t[t[index]] += 1
        return dict_for_s == dict_for_t


