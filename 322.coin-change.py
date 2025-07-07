#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
from typing import List


# @lc code=start
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        # `amount` <= 1e4 in this problem
        INF = 100000
        # initialization: 0 coin to get amount 0
        dp = [0] + [INF] * amount

        # look for combinations, so coins iteration outside
        for coin in coins:
            for total in range(coin, amount + 1):
                dp[total] = min(dp[total], dp[total - coin] + 1)

        return dp[-1] if dp[-1] != INF else -1


# @lc code=end
