'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Explanation:
The strings s and t can be made identical by:
    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false

Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        define a dictionary to maintain a pattern to word pair, s = word, t = pattern.
        check len(s) == len(t) return false if not equal
        iterate through s, if letter in s not in dictionary add s as key and t and value via t[index]
        if letter in s IS in dictionary, check if t[index] is equal to dict[letter] return false if not equal.
        do the same as above except t = word and s = pattern.
        '''

        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for index, letter in enumerate(s):
            if letter not in s_to_t:
                s_to_t[letter] = t[index]
            else:
                if s_to_t[letter] != t[index]:
                    return False

            if t[index] not in t_to_s:
                t_to_s[t[index]] = letter
            else:
                if t_to_s[t[index]] != letter:
                    return False
        return True