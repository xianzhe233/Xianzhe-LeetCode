#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#
from typing import List


# @lc code=start
class Solution:

    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        ans = 1
        last_diff = 0
        diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

        for diff in diffs:
            # signs of two diffs are different
            if diff * last_diff < 0 or (last_diff == 0 and diff):
                ans += 1

            last_diff = diff

        # an arbitrary number can always be in wiggle sequence
        return ans


# @lc code=end
nums = [1, 7, 4, 9, 2, 1]
print(Solution().wiggleMaxLength(nums))
