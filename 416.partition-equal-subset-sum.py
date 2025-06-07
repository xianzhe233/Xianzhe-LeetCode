#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from typing import List


# @lc code=start
class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # no possible partition
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2

        # dp[space]: the maximum value of picking the first `i` numbers to fill a backpack of capacity `space`
        # `i` is determined by the iteration
        dp = [0] * (target_sum + 1)
        for num in nums:
            for space in range(target_sum, num - 1, -1):
                # do not pick this number: inherit from the previous value
                # pick this number: use a space of `num` and gain a value of `num`
                dp[space] = max(dp[space], dp[space - num] + num)

        return dp[-1] == target_sum


# @lc code=end
Solution().canPartition([2, 2, 1, 1])
