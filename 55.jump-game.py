#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
from typing import List


# @lc code=start
class Solution:

    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for pos, jump_range in enumerate(nums):
            if pos > farthest:
                return False
            farthest = max(pos + jump_range, farthest)

        return True


# @lc code=end
