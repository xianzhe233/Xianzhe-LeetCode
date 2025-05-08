#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List


# @lc code=start
class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = []
        used = [False] * len(nums)

        def perm_generator(total):
            # base case
            if total == len(nums):
                yield perm[:]
                return

            for i, num in enumerate(nums):
                # use current number
                if not used[i]:
                    used[i] = True
                    perm.append(num)
                    yield from perm_generator(total + 1)
                    perm.pop()
                    used[i] = False

        return list(perm_generator(0))


# @lc code=end
