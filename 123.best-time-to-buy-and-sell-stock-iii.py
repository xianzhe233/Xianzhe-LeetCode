#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
from typing import List


# @lc code=start
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        # dp[i][num_trans]: maximum profit at `i`th day with `num_trans` transactions done
        dp = [[0 for _ in range(3)] for _ in range(N + 1)]

        for num_trans in (1, 2):

            # best profit before `i`th day
            diff = -prices[0]
            for i in range(1, N + 1):
                # total profit if sell the stock today
                # diff = previous_profit - new_bought_stock_value
                # sell_profit = price_at_ith_day - new_bought_stock_value + previous_profit = total_profit
                sell_profit = prices[i - 1] + diff

                # to sell or not to sell
                dp[i][num_trans] = max(dp[i - 1][num_trans], sell_profit)

                if i < N:
                    diff = max(diff, dp[i][num_trans - 1] - prices[i])

        # 2 transactions includes other situations
        return dp[N][2]


# @lc code=end
Solution().maxProfit([6, 1, 3, 2, 4, 7])
