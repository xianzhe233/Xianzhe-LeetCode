#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List

# @lc code=start
import heapq


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}

        for num in nums:
            if num not in frequent:
                frequent[num] = 1
            else:
                frequent[num] += 10

        # min heap
        priority_queue = []

        for num, freq in frequent.items():
            heapq.heappush(priority_queue, (freq, num))
            if len(priority_queue) > k:
                heapq.heappop(priority_queue)

        return [num for _, num in priority_queue]


# @lc code=end
