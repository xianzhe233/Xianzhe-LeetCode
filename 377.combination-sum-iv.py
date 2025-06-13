#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
from typing import List


# @lc code=start
class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = [1] + [0] * target

        # find permutations, so space first
        for space in range(target + 1):
            for num in nums:
                if space >= num:
                    dp[space] += dp[space - num]

        # dp[target]
        return dp[-1]


# @lc code=end
