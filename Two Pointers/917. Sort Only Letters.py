"""
Given a string s, reverse the string according to the following rules:
    All the characters that are not English letters remain in the same position.
    All the English letters (lowercase or uppercase) should be reversed.

Return s after reversing it.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        left: int = 0
        right: int = len(s) - 1

        new_s = list(s)

        while left < right:
            if not new_s[left].isalpha():
                left += 1
            elif not new_s[right].isalpha():
                right -= 1
            else:
                new_s[left], new_s[right] = new_s[right], new_s[left]
                left += 1
                right -= 1

        return "".join(new_s)