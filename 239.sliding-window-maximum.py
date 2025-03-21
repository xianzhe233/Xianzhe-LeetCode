#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
from collections import deque
from typing import List

# @lc code=start


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        window = deque()

        for i, num in enumerate(nums):
            # if former nums in window are not as great as new number,
            # they can't be the maximum in the window
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(i)

            # clean old maximum out of window
            if window[0] <= i - k:
                window.popleft()

            # begin to record answers after first window position
            if i >= k - 1:
                ans.append(nums[window[0]])

        return ans


# @lc code=end
