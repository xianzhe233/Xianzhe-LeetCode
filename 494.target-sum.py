#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List


# @lc code=start
class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # because there's negative numbers, a positive shift number is needed
        shift = sum(nums)

        if abs(target) > shift:
            return 0

        # dp[sum]: number of different ways using first `i` nums to get `sum`
        # `i` is determined by iteration
        dp = [[0] * (shift * 2 + 1) for _ in range(len(nums) + 1)]
        # at the beginning, there's no number, so one way to get sum 0
        dp[0][0 + shift] = 1

        for i, num in enumerate(nums, 1):
            for current_sum in range(shift + shift + 1):

                ways = 0

                if current_sum - num >= 0:
                    ways += dp[i - 1][current_sum - num]

                if current_sum + num <= 2 * shift:
                    ways += dp[i - 1][current_sum + num]

                dp[i][current_sum] = ways

        return dp[-1][target + shift]


# @lc code=end
