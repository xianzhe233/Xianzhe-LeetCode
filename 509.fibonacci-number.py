#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#


# @lc code=start
class Solution:

    def fib(self, n: int) -> int:
        f_0 = 0
        f_1 = 1

        if n == 0:
            return f_0
        if n == 1:
            return f_1

        num_steps = n - 1

        for _ in range(num_steps):
            f_0, f_1 = f_1, f_0 + f_1

        return f_1


# @lc code=end
