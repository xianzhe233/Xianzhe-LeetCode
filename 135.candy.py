#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
from typing import List


# @lc code=start
class Solution:

    def candy(self, ratings: List[int]) -> int:
        candies_left = [1]
        candies_right = [1]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies_left.append(candies_left[-1] + 1)
            else:
                candies_left.append(1)

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies_right.append(candies_right[-1] + 1)
            else:
                candies_right.append(1)

        return sum([
            max(left, right)
            for left, right in zip(candies_left, candies_right[::-1])
        ])


# @lc code=end
