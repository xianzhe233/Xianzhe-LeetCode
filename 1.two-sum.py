#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List


# @lc code=start
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary: dict[int, int] = {}
        for i, v in enumerate(nums):
            if target - v in dictionary.keys():
                return [i, dictionary[target - v]]
            dictionary.update({v: i})
        return []


# @lc code=end
