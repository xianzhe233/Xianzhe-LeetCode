#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
from typing import List


# @lc code=start
class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # pruning
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                k, l = j + 1, n - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if sum > target:
                        l -= 1
                    elif sum < target:
                        k += 1
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1

        return ans


# @lc code=end
