#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List


# @lc code=start
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        # state: largest_sum[index]
        # largest_sum: largest sum of subarrays that end at `index`
        # index: index of `nums`

        # every num itself is a subarray
        largest_sum = nums[:]

        for i, num in enumerate(nums[1:], start=1):
            if largest_sum[i - 1] > 0:
                largest_sum[i] += largest_sum[i - 1]

        return max(largest_sum)


# @lc code=end
