#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
from typing import List


# @lc code=start
class Solution:
    # rob function from house-robber-i
    def robber(self, nums: List[int]) -> int:
        dp = [0, 0]

        for money in nums:
            dp[0], dp[1] = max(dp[0], dp[1]), max(dp[1], dp[0] + money)

        return max(dp)

    def rob(self, nums: List[int]) -> int:
        # special case: only 1 house in the street
        if len(nums) <= 1:
            return sum(nums)
        return max(self.robber(nums[1:]), self.robber(nums[:-1]))


# @lc code=end
