'''
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
Specifically:
    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
    'a' maps to "dog".
    'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        Define a hashmap to store word-letter pair (letter is the key).
        if len(pattern) != len(s.split(" ")) return false
        iterate through pattern, if word not in dict, add word to dict as key with letter as value (using the same index)
        if word in dict, check if letter in s is the same as the value of that key (word) in the dict, if its different, return false.
        '''

        p_t_w = {}
        w_t_p = {}

        s = s.split(" ")

        if len(pattern) != len(s):   return False

        for index, letter in enumerate(pattern):
            if letter not in p_t_w:
                p_t_w[letter] = s[index]
            else:
                if p_t_w[letter] != s[index]:
                    return False

            if s[index] not in w_t_p:
                w_t_p[s[index]] = letter
            else:
                if w_t_p[s[index]] != letter:
                    return False
        return True