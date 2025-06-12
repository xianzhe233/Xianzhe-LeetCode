#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#
from typing import List


# @lc code=start
class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][temp_amount]: num of distinct ways to get `temp_amount` money using first `i` coins.
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        dp[0][0] = 1

        for i, coin in enumerate(coins, 1):
            for temp_amount in range(amount + 1):
                if coin > temp_amount:
                    # unable use this coin
                    dp[i][temp_amount] = dp[i - 1][temp_amount]
                else:
                    # don't use this coin, or use this coin
                    dp[i][temp_amount] = dp[i - 1][temp_amount] + dp[i][
                        temp_amount - coin]

        # dp[len(coins)][amount]
        return dp[-1][-1]


# @lc code=end
