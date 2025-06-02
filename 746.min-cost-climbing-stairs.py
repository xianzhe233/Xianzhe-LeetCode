#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
from typing import List


# @lc code=start
class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top is 1 step after last index in `cost`
        N = len(cost)

        # min_cost[index]: min cost to reach `index`
        # at the beginning, min cost to every place is +infinity
        # can start from index 0 or 1
        min_cost = [0] * 3

        for i in range(2, N + 1):
            # get here from 1 step behind or 2 steps behind
            min_cost[2] = min(min_cost[2 - 1] + cost[i - 1],
                              min_cost[2 - 2] + cost[i - 2])
            min_cost[1], min_cost[0] = min_cost[2], min_cost[1]

        return min_cost[2]


# @lc code=end
