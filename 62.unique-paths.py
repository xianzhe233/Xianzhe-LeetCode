#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
from math import comb


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        # C(m - 1, m + n - 2)
        # m + n - 2 steps: (m - 1) steps down and (n - 1) steps right in total
        # m - 1 combinations: choose which (m - 1) steps to go down, it's ok with (n - 1)
        return comb(m + n - 2, m - 1)


# @lc code=end
