#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
from typing import List


# @lc code=start
class Solution:

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int],
                     nums4: List[int]) -> int:
        dictionary = {}
        for a in nums1:
            for b in nums2:
                if a + b not in dictionary:
                    dictionary[a + b] = 1
                else:
                    dictionary[a + b] += 1

        ans = 0
        for c in nums3:
            for d in nums4:
                if -(c + d) in dictionary:
                    ans += dictionary[-(c + d)]

        return ans


# @lc code=end
