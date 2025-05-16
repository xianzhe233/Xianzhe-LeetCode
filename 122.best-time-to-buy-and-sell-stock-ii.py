#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import List


# @lc code=start
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        diffs = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

        return sum([diff for diff in diffs if diff > 0])


# @lc code=end
