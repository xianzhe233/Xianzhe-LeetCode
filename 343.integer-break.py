#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#


# @lc code=start
class Solution:

    def integerBreak(self, n: int) -> int:

        # max_product[x]: maximum of products of integers that `x` breaks into.
        # initialization: every number can break into 1's and get product 1, 1 is minimum
        max_product = [max(i - 1, 1) for i in range(n + 1)]

        for num in range(2, n + 1):
            # avoid repeating
            # for example: 5 = 2 + 3 = 3 + 2
            for part1 in range(1, num // 2 + 1):
                part2 = num - part1
                max_product[num] = max(
                    max_product[num],
                    max(max_product[part1], part1) *
                    max(max_product[part2], part2))

        return max_product[n]


# @lc code=end
