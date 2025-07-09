#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
from typing import List


# @lc code=start
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)

        # initialization: empty word is always available
        dp = [True] + [False] * N

        for length in range(1, N + 1):
            sub_str = s[:length]
            for word in wordDict:
                if sub_str.endswith(word):
                    dp[length] |= dp[length - len(word)]

        # dp[N]
        return dp[-1]


# @lc code=end
