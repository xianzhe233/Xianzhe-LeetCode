#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
from typing import List


# @lc code=start
class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def get_num_dict():
            num_dict = {}
            for num in nums:
                if num not in num_dict:
                    num_dict[num] = 0

                num_dict[num] += 1
            return num_dict

        perm = []
        num_dict = get_num_dict()

        def perm_generator(total, last=None):
            nonlocal perm, num_dict

            # base case
            if total == len(nums):
                yield perm[:]
                return

            for num, amount in num_dict.items():
                # prevent repeating perms
                if num == last:
                    continue

                if amount == 0:
                    continue

                for quota in range(1, amount + 1):
                    num_dict[num] -= quota
                    perm += [num] * quota
                    yield from perm_generator(total + quota, num)
                    num_dict[num] += quota
                    perm = perm[:-(quota)]

        return list(perm_generator(0))


# @lc code=end
