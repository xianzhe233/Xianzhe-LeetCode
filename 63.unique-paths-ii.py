#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
from typing import List


# @lc code=start
class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # initialize:
        # if there're obstacles at the first row, num_path of themselves and right grid are all 0's
        # otherwise, num_path are 1's
        try:
            first_obstacle_index = obstacleGrid[0].index(1)
            num_path = [0 if i >= first_obstacle_index else 1 for i in range(n)]
        except:
            num_path = [1] * n

        for x in range(1, m):
            # special: need to deal with obstacles at (x, 0) because they will affect calculations after them
            if obstacleGrid[x][0]:
                num_path[0] = 0
            for y in range(1, n):
                # blocked grids, 0 path
                if obstacleGrid[x][y]:
                    num_path[y] = 0
                else:
                    num_path[y] = num_path[y] + num_path[y - 1]

        # num_path[n - 1]
        return num_path[-1]


# @lc code=end
