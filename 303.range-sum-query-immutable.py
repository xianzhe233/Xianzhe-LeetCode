#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
from typing import List

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = nums
        for i in range(1, len(self.sums)):
            self.sums[i] += self.sums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

