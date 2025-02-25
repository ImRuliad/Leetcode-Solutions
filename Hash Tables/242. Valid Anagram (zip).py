'''
Given two strings s and t, return true if t is an of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq_s = {}
        freq_t = {}

        for letter_s, letter_t in zip(s, t):
            if letter_s not in freq_s:
                freq_s[letter_s] = 1
            else:
                freq_s[letter_s] += 1

            if letter_t not in freq_t:
                freq_t[letter_t] = 1
            else:
                freq_t[letter_t] += 1

        return freq_t == freq_s
