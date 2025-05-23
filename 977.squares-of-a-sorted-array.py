#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def getGreatestSquare(self, nums, l, r):
        lSquare, rSquare = nums[l] ** 2, nums[r] ** 2
        if lSquare > rSquare:
            return lSquare, l + 1, r
        else:
            return rSquare, l, r - 1

    def sortedSquares(self, nums: List[int]) -> List[int]:
        newList = [0] * len(nums)
        l, r = 0, len(nums) - 1
        for i in range(len(newList) - 1, -1, -1):
            newList[i], l, r = self.getGreatestSquare(nums, l, r)
        return newList
        # return sorted(num ** 2 for num in nums)
        
# @lc code=end

