#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
from string import ascii_lowercase
from typing import List


# @lc code=start
class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        alphabet_right_bounds = {}

        for char in ascii_lowercase:
            try:
                alphabet_right_bounds[char] = s.rindex(char)
            except:
                pass

        ans = []
        farthest = -1
        last_end = -1

        for i, char in enumerate(s):
            right = alphabet_right_bounds[char]
            farthest = max(farthest, right)

            if i >= farthest:
                ans.append(i - last_end)
                last_end = i

        return ans


# @lc code=end
