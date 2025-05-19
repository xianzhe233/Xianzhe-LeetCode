#
# @lc app=leetcode id=1005 lang=python3
#
# [1005] Maximize Sum Of Array After K Negations
#
from typing import List
import heapq


# @lc code=start
class Solution:

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(k):
            smallest = heapq.heappop(nums)
            heapq.heappush(nums, -smallest)

        return sum(nums)


# @lc code=end
