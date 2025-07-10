#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List


# @lc code=start
class Solution:

    def rob(self, nums: List[int]) -> int:
        # simplified version of dp[house_id][True/False]: max value of robbing all houses before `house_id`(included) with `house_id`th house robbed/not robbed
        # this simplified version just keep one step's information cause that's all we need
        dp = [0, 0]

        for money in nums:
            # not rob: inherit money before
            # rob it!: inherit money before, or rob this house without robbing the last
            dp[0], dp[1] = max(dp[0], dp[1]), max(dp[1], dp[0] + money)

        # rob last house or not gives different answers, we need the greater one
        return max(dp)


# @lc code=end
