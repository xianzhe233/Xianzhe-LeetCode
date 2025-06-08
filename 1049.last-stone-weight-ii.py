#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#
from typing import List


# @lc code=start
class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:

        total_sum = sum(stones)
        target_sum = total_sum // 2

        # dp[space]: the maximum value of picking the first `i` stones to fill a backpack of capacity `space`
        # `i` is determined by the iteration
        dp = [0] * (target_sum + 1)
        for stone in stones:
            for space in range(target_sum, stone - 1, -1):
                # do not pick this stone: inherit from the previous value
                # pick this stone: use a space of `stone` and gain a value of `stone`
                dp[space] = max(dp[space], dp[space - stone] + stone)

        # heavy stone set - light stone set
        # (total_sum - light_stone_set_weight) - light_stone_set_weight
        # light_stone_set_weight = dp[target_sum] = dp[-1]
        return total_sum - 2 * dp[-1]


# @lc code=end
