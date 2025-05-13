#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#
from typing import List


# @lc code=start
class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        ans = 0
        child_idx = 0
        cookie_idx = 0

        while child_idx < len(g) and cookie_idx < len(s):
            child_val = g[child_idx]
            cookie_val = s[cookie_idx]

            if cookie_val >= child_val:
                ans += 1
                child_idx, cookie_idx = child_idx + 1, cookie_idx + 1
            else:
                # this cookie can't satisfy any child anymore, so try to find next useful cookie
                while cookie_idx < len(s) and s[cookie_idx] < child_val:
                    cookie_idx += 1

        return ans


# @lc code=end
