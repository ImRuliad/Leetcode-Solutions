'''
Given a string s, return true if s is a good string, or false otherwise.
A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

Example 1:
Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

Example 2:
Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
'''


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occurences = {}

        for letter in s:
            if letter not in occurences:
                occurences[letter] = 1
            else:
                occurences[letter] += 1

        first_frequency = occurences[letter]

        for frequency in occurences.values():
            if first_frequency != frequency:
                return False
        return True