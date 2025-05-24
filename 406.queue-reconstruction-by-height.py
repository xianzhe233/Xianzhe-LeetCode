#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
from typing import List


# @lc code=start
class Solution:

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # height: large -> small
        # rank: small -> large
        people.sort(key=lambda p: (-p[0], p[1]))

        for i in range(len(people)):
            rank = people[i][1]

            # correct position
            if i == rank:
                continue

            people.insert(rank, people.pop(i))

        return people


# @lc code=end
