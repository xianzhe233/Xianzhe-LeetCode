#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#


# @lc code=start
class Solution:

    def reverseStr(self, s: str, k: int) -> str:
        new_str = list(s)
        for i in range(0, len(s), 2 * k):
            if i + k <= len(s):
                new_str[i:i + k] = s[i:i + k][::-1]
            else:
                new_str[i:len(s)] = s[i:len(s)][::-1]
        return "".join(new_str)


# @lc code=end
