#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#


# @lc code=start
class Solution:

    def reverseWords(self, s: str) -> str:
        return " ".join(list(reversed(list(s.strip().split()))))


# @lc code=end
