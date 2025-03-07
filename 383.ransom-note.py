#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#


# @lc code=start
class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict: dict[str, int] = {}
        note_dict: dict[str, int] = {}

        for c in magazine:
            if c in magazine_dict:
                magazine_dict[c] += 1
            else:
                magazine_dict[c] = 1

        for c in ransomNote:
            if c in note_dict:
                note_dict[c] += 1
            else:
                note_dict[c] = 1

        return all([
            c in magazine_dict and magazine_dict[c] >= note_dict[c]
            for c in note_dict
        ])


# @lc code=end
