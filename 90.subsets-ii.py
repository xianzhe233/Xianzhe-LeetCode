#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
from typing import List

# @lc code=start


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset = []

        def subset_generator(index):
            # base case
            if index == len(nums):
                yield subset.copy()
                return

            num = nums[index]

            # choose not to add this number and the same numbers anymore
            next_index = index + 1
            # find next number that is not the same as this
            while next_index < len(nums) and nums[next_index] == num:
                next_index += 1
            yield from subset_generator(next_index)

            # choose to add this number
            subset.append(num)
            yield from subset_generator(index + 1)
            subset.pop()

        return list(subset_generator(0))


# @lc code=end
