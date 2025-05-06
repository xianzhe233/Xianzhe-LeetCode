#
# @lc app=leetcode id=491 lang=python3
#
# [491] Non-decreasing Subsequences
#
from typing import List


# @lc code=start
class Solution:

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # Non-decreasing subsequence
        nds = []
        banned = set()

        def valid(index):
            nonlocal nds, banned

            # if subsequence is empty, any number is ok
            if not nds:
                return True

            # non-decreasing and not banned
            return nds[-1] <= nums[index] and nums[index] not in banned

        def nds_generator(index):
            nonlocal nds, banned

            # base case
            if index == len(nums):
                if len(nds) >= 2:
                    yield nds[:]
                return

            num = nums[index]

            if valid(index):
                # allow to use this number
                nds.append(num)
                yield from nds_generator(index + 1)
                nds.pop()

                # choose to not use this number
                banned.add(num)
                yield from nds_generator(index + 1)
                if num in banned:
                    banned.remove(num)
            else:
                # if break non-decreasing, skip this number
                yield from nds_generator(index + 1)

        return list(nds_generator(0))


# @lc code=end
