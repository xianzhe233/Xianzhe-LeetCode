#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List


# @lc code=start
class Solution:
    num_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        comb = []

        def dfs(index):
            nonlocal comb

            if index >= len(digits):
                yield "".join(comb[:])
                return

            for letter in Solution.num_map[digits[index]]:
                comb.append(letter)
                yield from dfs(index + 1)
                comb.pop()

        if not digits:
            return []
        return list(dfs(0))


# @lc code=end
