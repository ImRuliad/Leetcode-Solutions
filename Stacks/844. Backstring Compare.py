"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
    Input: s = "ab#c", t = "ad#c"
    Output: true
    Explanation: Both s and t become "ac".

Example 2:
    Input: s = "ab##", t = "c#d#"
    Output: true
    Explanation: Both s and t become "".

Example 3:
    Input: s = "a#c", t = "b"
    Output: false
    Explanation: s becomes "c" while t becomes "b".

"""



class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        brute force approach:
        create new lists for s and t
        iterate through s and t

        if a char is encountered push onto stack
        if a # is encountered pop from the stack

        return new_s == new_t

        '''

        new_s: str = []
        new_t: str = []

        for letter in s:
            if letter != "#":
                new_s.append(letter)
            elif new_s:
                new_s.pop()

        for letter in t:
            if letter != "#":
                new_t.append(letter)
            elif new_t:
                new_t.pop()

        return new_s == new_t