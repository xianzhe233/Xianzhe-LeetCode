#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#
from math import inf
from typing import List


# @lc code=start
class Solution:

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_length = 0
        current_length = 0
        last_num = -inf

        for num in nums:
            if num > last_num:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1
            last_num = num

        return max_length


# @lc code=end
