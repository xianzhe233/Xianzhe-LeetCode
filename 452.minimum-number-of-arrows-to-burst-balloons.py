#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#
from typing import List


# @lc code=start
class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        INF = 2**31 + 1

        points = sorted(points, key=lambda p: p[1])
        ans = 0
        last_arrow = -INF

        for left, right in points:
            if left > last_arrow:
                last_arrow = right
                ans += 1

        return ans


# @lc code=end
