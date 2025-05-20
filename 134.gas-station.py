#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
from typing import List


# @lc code=start
class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        INF = int(1e10)

        increments = [gas_i - cost_i for gas_i, cost_i in zip(gas, cost)]

        # no enough gas to travel around
        if sum(increments) < 0:
            return -1

        min_tank = INF
        tank = 0
        station = -1

        for i, increment in enumerate(increments):
            tank += increment

            if min_tank > tank:
                min_tank = tank
                ans = (i + 1) % len(increments)  # circulate

        return ans


# @lc code=end
