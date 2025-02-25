'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        define two hashmap for occurences of ransomNote and magazine.
        iterate through both add letter to key and occurence as value
        if letter not in hashmap dict(letter) = 1 else dict(letter) += 1
        compare occurences.
        '''
        count = defaultdict(int)

        for letter in magazine:
            count[letter] += 1

        for letter in ransomNote:
            if count[letter] == 0 or letter not in magazine:
                return False
            count[letter] -= 1
        return True