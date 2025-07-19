#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
from functools import cache
from math import inf
from typing import List

# @lc code=start


class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)

        @cache
        def profit(day, hold):
            if day < 0:
                return -inf if hold else 0

            if hold:
                return max(profit(day - 1, True),
                           profit(day - 1, False) - prices[day])
            else:
                return max(profit(day - 1, False),
                           profit(day - 1, True) + prices[day] - fee)

        return profit(N - 1, False)


# @lc code=end
