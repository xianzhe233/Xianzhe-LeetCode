#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List


# @lc code=start
class Solution:

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        candidates.sort()
        comb = []

        def generate_comb(total, lower_bound_index):

            # base case
            if total == 0:
                yield comb[:]
                return

            if lower_bound_index >= len(candidates):
                return

            candidate = candidates[lower_bound_index]

            # pruning: even smallest number is greater than total target, there's no chance to get a valid comb then
            if candidate > total:
                return

            # skip this candidate
            yield from generate_comb(total, lower_bound_index + 1)

            # use this candidate and keep it
            comb.append(candidate)
            yield from generate_comb(total - candidate, lower_bound_index)

            comb.pop()

        if not candidates:
            return []

        return list(generate_comb(target, 0))


# @lc code=end
