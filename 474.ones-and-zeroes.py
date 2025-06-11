#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
from typing import List


# @lc code=start
class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        def extract_bin():
            zero_ones = []
            for string in strs:
                num_zero = string.count('0')
                num_one = string.count('1')
                zero_ones.append((num_zero, num_one))
            return zero_ones

        zero_ones = extract_bin()

        # dp[zero][one]: maximum size of strings which have at most `zero` zeros and `one` ones using first `i` strings. `i` is determined by iteration
        # initialization: at the beginning, we can get maximum size of 0 with first 0 strings (no string)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for zero_one_tuple in zero_ones:
            zeros, ones = zero_one_tuple
            for num_zero in range(m, zeros - 1, -1):
                for num_one in range(n, ones - 1, -1):
                    dp[num_zero][num_one] = max(
                        dp[num_zero][num_one],
                        dp[num_zero - zeros][num_one - ones] + 1)

        # dp[m][n]
        return dp[-1][-1]


# @lc code=end
Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
