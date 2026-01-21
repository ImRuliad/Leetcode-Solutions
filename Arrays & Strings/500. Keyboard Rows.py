"""
Given an array of strings words:
return the words that can be typed using letters of the alphabet on only one row of American keyboard.
Note that the strings are case-insensitive:
both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl",
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Explanation:
Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
"""
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row: set = set("qwertyuiop")
        second_row: set = set("asdfghjkl")
        third_row: set = set("zxcvbnm")

        result_words: list[str] = []
        for word in words:
            word_set = set(word.lower())
            if word_set <= first_row or word_set <= second_row or word_set <= third_row:
                result_words.append(word)
        return result_words