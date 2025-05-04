#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List

# @lc code=start
from itertools import combinations


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:

        def subset_generator():
            for length in range(len(nums) + 1):
                for comb in combinations(nums, length):
                    yield comb

        return list(subset_generator())


# @lc code=end
