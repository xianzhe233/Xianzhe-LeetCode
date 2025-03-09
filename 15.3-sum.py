#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from enum import unique
from typing import List


# @lc code=start
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            x = nums[i]
            # except identical tuples for x
            if i > 0 and x == nums[i - 1]:
                continue

            if x + nums[i + 1] + nums[i + 2] > 0:
                break
            if x + nums[-2] + nums[-1] < 0:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                y, z = nums[j], nums[k]
                sum = x + y + z
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    ans.append([x, y, z])
                    j += 1
                    # except identical tuples for y
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1

        return ans


# @lc code=end
