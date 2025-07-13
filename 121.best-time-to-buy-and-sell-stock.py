#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from math import inf
from typing import List


# @lc code=start
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        low_point = inf
        ans = 0

        # greedy
        for price in prices:
            low_point = min(low_point, price)
            ans = max(ans, price - low_point)

        return ans


# @lc code=end
