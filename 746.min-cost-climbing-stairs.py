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
        N = len(cost) + 1
        INF = int(1e7)

        # min_cost[index]: min cost to reach `index`
        # at the beginning, min cost to every place is +infinity
        min_cost = [INF] * N
        # can start from index 0 or 1
        min_cost[0] = min_cost[1] = 0

        for i in range(2, N):
            # get here from 1 step behind or 2 steps behind
            min_cost[i] = min(min_cost[i], min_cost[i - 1] + cost[i - 1],
                              min_cost[i - 2] + cost[i - 2])

        return min_cost[-1]


# @lc code=end
