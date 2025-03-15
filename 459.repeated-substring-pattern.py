#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#


# @lc code=start
class Solution:

    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s * 2)[1:-1].find(s) != -1


# @lc code=end
