#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
from typing import List


# @lc code=start
class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort `intervals` by left bound
        intervals = sorted(intervals, key=lambda interval: interval[0])

        res = []
        current_farthest = intervals[0][1]
        current_left = intervals[0][0]

        for left, right in intervals:
            if left > current_farthest:
                res.append([current_left, current_farthest])
                current_left = left

            current_farthest = max(current_farthest, right)

        # add last term to `res`
        res.append([current_left, current_farthest])

        return res


# @lc code=end
