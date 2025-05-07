#
# @lc app=leetcode id=491 lang=python3
#
# [491] Non-decreasing Subsequences
#
from typing import List


# @lc code=start
class Solution:

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        pres = {(nums[0],)}
        for num in nums[1:]:
            pres.update({pre + (num,) for pre in pres if num >= pre[-1]})
            pres.add((num,))

        return [list(sequence) for sequence in pres if len(sequence) >= 2]


# @lc code=end
