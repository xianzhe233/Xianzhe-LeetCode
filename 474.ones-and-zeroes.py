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

        # dp[str_index][zero][one]: maximum size of strings which have at most `zero` zeros and `one` ones
        dp = [
            [[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)
        ]

        for str_index, zero_one_tuple in enumerate(zero_ones, 1):
            zeros, ones = zero_one_tuple
            for num_zero in range(m + 1):
                for num_one in range(n + 1):
                    dp[str_index][num_zero][num_one] = dp[str_index -
                                                          1][num_zero][num_one]

                    if num_zero >= zeros and num_one >= ones:
                        dp[str_index][num_zero][num_one] = max(
                            dp[str_index][num_zero][num_one],
                            dp[str_index - 1][num_zero - zeros][num_one - ones]
                            + 1)

        return dp[-1][-1][-1]


# @lc code=end
Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
