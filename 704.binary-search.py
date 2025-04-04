#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (int) ((l + r) / 2)
            if nums[mid] == target:
                return mid
            else:
                if target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
        
# @lc code=end

