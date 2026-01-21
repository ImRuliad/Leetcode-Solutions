"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        seen = set()
        s_size = len(s)-1
        longest_ss = 1

        if s_size < 0:  return 0

        while end <= s_size:
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
                current_ss = end-start
                longest_ss = max(longest_ss, current_ss)
            else:
                while s[end] in seen:
                    seen.remove(s[start])
                    start += 1
        return longest_ss
        