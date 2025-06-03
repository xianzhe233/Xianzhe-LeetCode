#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lc code=start
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        # num_path[x][y]: num of distinct paths to grid[x][y]
        num_path = [[1] * n for _ in range(m)]

        for x in range(1, m):
            for y in range(1, n):
                # get here from left or up
                num_path[x][y] = num_path[x - 1][y] + num_path[x][y - 1]

        # print
        for row in num_path:
            print(row)

        # num_path[m-1][n-1]
        return num_path[-1][-1]


# @lc code=end
