#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:

    def climbStairs(self, n: int) -> int:
        # 1 way to height 0, 1 way to height 1
        num_ways = [1, 1]

        for _ in range(2, n + 1):
            num_ways.append(num_ways[-1] + num_ways[-2])

        return num_ways[n]


# @lc code=end
