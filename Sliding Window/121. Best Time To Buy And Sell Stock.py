"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        element -> price of stock, index -> the day
        must buy before you sell.
        if window end < window start -> window start = window end
            increment window end by 1.
        if window end > window start -> get difference window_end - window_start
            maintain this difference in max()
        as long as the window end > window start increment window end + 1
        """

        start_window = 0
        max_diff = 0

        for end_window in range(1, len(prices)):
            if prices[end_window] > prices[start_window]:
                diff = prices[end_window] - prices[start_window]
                max_diff = max(max_diff, diff)
            else:
                start_window = end_window
        return max_diff