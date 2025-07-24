#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#


# @lc code=start
class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)

        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                # if new characters match, append old sequence
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # otherwise, inherit old sequence
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # dp[N][M]
        return dp[-1][-1]


# @lc code=end
