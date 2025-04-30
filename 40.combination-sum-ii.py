#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from typing import List


# @lc code=start
class Solution:

    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        if not candidates:
            return []

        candidates.sort()

        comb = []

        def generate_comb(index, total):
            if total == 0:
                yield comb[:]
                return

            if total < 0:
                return

            if index >= len(candidates):
                return

            next_idx = index
            while next_idx < len(
                    candidates) and candidates[index] == candidates[next_idx]:
                next_idx += 1

            # never use this number after this
            if next_idx < len(candidates):
                yield from generate_comb(next_idx, total)

            # allow to use current candidate
            candidate = candidates[index]
            comb.append(candidate)
            yield from generate_comb(index + 1, total - candidate)
            comb.pop()

        return list(generate_comb(0, target))


# @lc code=end
