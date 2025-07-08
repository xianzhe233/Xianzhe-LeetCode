#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
from math import sqrt


class Solution:

    def numSquares(self, n: int) -> int:
        # 1 <= n <= 10^4 in this problem
        INF = 10**9
        # all numbers that we will use in potential
        nums = [i**2 for i in range(1, int(sqrt(n)) + 1)]
        # initialization: 0 numbers to add up to 0
        dp = [0] + [INF] * n

        # look for combinations, so num iteration outside
        for num in nums:
            for space in range(num, n + 1):
                dp[space] = min(dp[space], dp[space - num] + 1)

        # dp[n]
        return dp[-1]


# @lc code=end
