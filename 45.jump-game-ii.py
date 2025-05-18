#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
from typing import List


# @lc code=start
class Solution:

    def jump(self, nums: List[int]) -> int:
        INF = int(1e9)
        N = len(nums)

        steps = [INF] * N
        # start at index 0
        steps[0] = 0

        for pos, jump_range in enumerate(nums):
            for new_pos in range(pos, min(N, pos + jump_range + 1)):
                steps[new_pos] = min(steps[new_pos], steps[pos] + 1)

        return steps[N - 1]


# @lc code=end
