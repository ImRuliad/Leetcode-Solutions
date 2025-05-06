'''
Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.
Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.
The frequency of a letter x is the number of times it occurs in the string.

Example 1:
Input: word1 = "aaaa", word2 = "bccb"
Output: false
Explanation: There are 4 'a's in "aaaa" but 0 'a's in "bccb".
The difference is 4, which is more than the allowed 3.

Example 2:
Input: word1 = "abcdeef", word2 = "abaaacc"
Output: true
Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 1 time in word1 and 4 times in word2. The difference is 3.
- 'b' appears 1 time in word1 and 1 time in word2. The difference is 0.
- 'c' appears 1 time in word1 and 2 times in word2. The difference is 1.
- 'd' appears 1 time in word1 and 0 times in word2. The difference is 1.
- 'e' appears 2 times in word1 and 0 times in word2. The difference is 2.
- 'f' appears 1 time in word1 and 0 times in word2. The difference is 1.

Example 3:
Input: word1 = "cccddabba", word2 = "babababab"
Output: true
Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 2 times in word1 and 4 times in word2. The difference is 2.
- 'b' appears 2 times in word1 and 5 times in word2. The difference is 3.
- 'c' appears 3 times in word1 and 0 times in word2. The difference is 3.
- 'd' appears 2 times in word1 and 0 times in word2. The difference is 2.
'''
from collections import defaultdict


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        '''
        get frequency of word1 and word2 using Counter
        use zip() to iterate through count of word1 and word2 frequencies.
        get abs val of difference between each words frequency.
        if abs val diff > 3 return false
        if iteration completes return true
        '''

        word1_freq = defaultdict(int)
        word2_freq = defaultdict(int)

        for element1, element2 in zip(word1, word2):
            if element1 not in word2:
                word2_freq[element1] = 0
            if element2 not in word1:
                word1_freq[element2] = 0

            word1_freq[element1] += 1
            word2_freq[element2] += 1

        for element1, element2 in zip(sorted(word1_freq), sorted(word2_freq)):
            print(element1, word1_freq[element1], element2, word2_freq[element2])

            diff = abs(word1_freq[element1] - word2_freq[element2])
            if diff > 3:
                return False
        return True

