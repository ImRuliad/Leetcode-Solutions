"""
Given a string s and an array of strings words, determine whether s is a prefix string of words.
A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.
Return true if s is a prefix string of words, or false otherwise.

Example 1:
Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.

Example 2:
Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.
"""
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        """
        """

        prefix_string = ""
        prefix_length = 0

        for word in words:
            prefix_string += word
            prefix_length += len(word)

            if prefix_length >= len(s):
                return prefix_string == s
        return False
            