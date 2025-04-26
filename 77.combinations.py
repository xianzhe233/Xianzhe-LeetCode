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

        def dfs(cur_comb, choices, rest=k):
            """
                `cur_comb`: generated combination till now
                `choices`: numbers that can be chosen
                `rest`: how many numbers can be added to comb
            """
            nonlocal res

            # base case
            if rest <= 0:
                res.append(cur_comb)
                return

            # if we have no choice, we are fail to get a comb
            if not choices:
                return

            for i, num in enumerate(choices):
                if len(choices) - i < rest:
                    break
                dfs(cur_comb + [num], choices[i + 1:], rest - 1)

        dfs([], list(range(1, n + 1)))

        return res


# @lc code=end
