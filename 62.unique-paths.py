#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lc code=start
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        # num_path[y]: num of distinct paths to grid[x][y], x depends on iteration
        num_path = [1] * n

        for x in range(1, m):
            for y in range(1, n):
                # get here from left or up
                # up: num_path[y]
                # left: num_path[y - 1]
                num_path[y] = num_path[y] + num_path[y - 1]

        # num_path[m-1][n-1]
        return num_path[-1]


# @lc code=end
