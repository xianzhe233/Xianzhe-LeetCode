#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
from typing import List


# @lc code=start
class Solution:

    def jump(self, nums: List[int]) -> int:

        ans = 0
        cur_farthest = 0
        next_farthest = 0

        for pos, jump_range in enumerate(nums[:-1]):
            next_farthest = max(next_farthest, pos + jump_range)
            if pos == cur_farthest:
                cur_farthest = next_farthest
                ans += 1

        return ans


# @lc code=end
