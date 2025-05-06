"""
You are given a 0-indexed integer array forts of length n representing the positions of several forts. forts[i] can be -1, 0, or 1 where:
-1 represents there is no fort at the ith position.
0 indicates there is an enemy fort at the ith position.
1 indicates the fort at the ith the position is under your command.

Now you have decided to move your army from one of your forts at position i to an empty position j such that:
0 <= i, j <= n - 1
The army travels over enemy forts only.
Formally, for all k where min(i,j) < k < max(i,j), forts[k] == 0.
While moving the army, all the enemy forts that come in the way are captured.
Return the maximum number of enemy forts that can be captured. In case it is impossible to move your army, or you do not have any fort under your command, return 0.



Example 1:
Input: forts = [1,0,0,-1,0,0,0,0,1]
Output: 4
Explanation:
    - Moving the army from position 0 to position 3 captures 2 enemy forts, at 1 and 2.
    - Moving the army from position 8 to position 3 captures 4 enemy forts.
    Since 4 is the maximum number of enemy forts that can be captured, we return 4.

Example 2:
Input: forts = [0,0,1,-1]
Output: 0
Explanation:
    Since no enemy fort can be captured, 0 is returned.
"""



#Solution could be more concise.
#Uses Two pointers + Kadanes Algorithm
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        slow = 0
        fast = 0

        max_forts_taken = 0
        amt_of_forts = len(forts) - 1

        while fast <= amt_of_forts:
            if forts[fast] == -1 and forts[slow] == 1:
                curr_forts_taken = ((fast + 1) - (slow + 1)) - 1
                max_forts_taken = max(max_forts_taken, curr_forts_taken)

            elif forts[fast] == 1 and forts[slow] == -1:
                curr_forts_taken = ((fast + 1) - (slow + 1)) - 1
                max_forts_taken = max(max_forts_taken, curr_forts_taken)

            if forts[fast] == 1 or forts[fast] == -1:
                slow = fast
            fast += 1

        print(max_forts_taken)
        return max_forts_taken