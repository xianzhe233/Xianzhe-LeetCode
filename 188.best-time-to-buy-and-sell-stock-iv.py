#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
from typing import List


# @lc code=start
class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0] * (k + 1) for _ in range(N + 1)]
        for num_trans in range(1, k + 1):
            diff = -prices[0]

            for i in range(1, N + 1):
                sell_profit = prices[i - 1] + diff

                dp[i][num_trans] = max(dp[i - 1][num_trans], sell_profit)

                if i < N:
                    diff = max(diff, dp[i][num_trans - 1] - prices[i])

        return dp[N][k]


# @lc code=end
