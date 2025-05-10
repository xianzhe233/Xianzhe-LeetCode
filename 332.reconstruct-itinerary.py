#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
from collections import defaultdict
import heapq
from typing import List


# @lc code=start
class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        destinations = defaultdict(list)
        for u, v in tickets:
            heapq.heappush(destinations[u], v)

        itinerary = []

        def dfs(airport):
            while destinations[airport]:
                next_dest = heapq.heappop(destinations[airport])
                dfs(next_dest)
            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]


# @lc code=end
