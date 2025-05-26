#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
from math import inf
from typing import List


# @lc code=start
class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda p: p[1])
        ans = len(intervals)
        last_right = -inf

        for left, right in intervals:
            if left >= last_right:
                ans -= 1
                last_right = right

        return ans


# @lc code=end
