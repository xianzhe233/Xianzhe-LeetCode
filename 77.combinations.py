#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
from typing import List


# @lc code=start
class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur_comb = []

        def dfs(lower_bound, rest=k):
            """
                `lower_bound`: smallest number that can be chosen, lower_bound <= choices <= n
                `rest`: how many numbers can be added to comb
            """
            nonlocal res, cur_comb

            # base case
            if rest <= 0:
                res.append(cur_comb.copy())
                return

            for num in range(lower_bound, n + 1):
                cur_comb.append(num)
                dfs(num + 1, rest - 1)
                cur_comb.pop()

        dfs(1)

        return res


# @lc code=end
