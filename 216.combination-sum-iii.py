#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
from typing import List


# @lc code=start
class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(n, lower_bound):
            nonlocal res, comb

            # base case
            if n == 0:
                if len(comb) == k:
                    res.append(comb.copy())

                return

            if len(comb) == k:
                return

            # pruning: If even largest nums can't sum to n, then fail
            if sum(list(range(10))[-(k - len(comb)):]) < n:
                return

            for num in range(lower_bound, 10):
                if n - num < 0:
                    break

                comb.append(num)
                dfs(n - num, num + 1)
                comb.pop()

        dfs(n, 1)

        return res


# @lc code=end
