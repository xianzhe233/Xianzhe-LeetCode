#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from typing import List


# @lc code=start
class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)

        # dp[i]: the longest length of strictly increasing subsequences that end with `i - 1`th number
        dp = [0] + [1] * N

        for i, num in enumerate(nums, 1):
            for last_i, last_num in enumerate(nums[:i], 1):
                if last_num < num:
                    dp[i] = max(dp[i], dp[last_i] + 1)

# the longest strictly increasing subsequences aren't always end with the last number, so choose the largest in the whole list
        return max(dp)


# @lc code=end
