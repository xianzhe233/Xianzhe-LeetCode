#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


# @lc code=start
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = [0] * 26
        t_dict = [0] * 26
        for character in s:
            s_dict[ord(character) - ord('a')] += 1
        for character in t:
            t_dict[ord(character) - ord('a')] += 1

        for cnt1, cnt2 in zip(s_dict, t_dict):
            if cnt1 != cnt2:
                return False

        return True


# @lc code=end
