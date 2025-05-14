#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:

    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        # states: seq_length[index][direction]
        # seq_length: longest length of wiggle sequences that end with nums[index]
        # index: index of a number in `nums`
        # direction: True for increment, False for decrement
        seq_length = defaultdict(dict)
        for i in range(len(nums)):
            # start from this number, length of sequence can always be 1
            seq_length[i][True] = 1
            seq_length[i][False] = 1

        # try to append sequence at `last_index` with number at `current_index`
        for current_index in range(1, len(nums)):
            for last_index in range(current_index):
                last_num, current_num = nums[last_index], nums[current_index]
                # a decreasing number can append an increasing-ended sequence
                if current_num < last_num:
                    seq_length[current_index][False] = max(
                        seq_length[current_index][False],
                        seq_length[last_index][True] + 1)
                # an increasing number can append a decreasing-ended sequence
                if current_num > last_num:
                    seq_length[current_index][True] = max(
                        seq_length[current_index][True],
                        seq_length[last_index][False] + 1)

        ans = max(seq_length[len(nums) - 1][True],
                  seq_length[len(nums) - 1][False])

        return ans


# @lc code=end
nums = [1, 7, 4, 9, 2, 1]
print(Solution().wiggleMaxLength(nums))
