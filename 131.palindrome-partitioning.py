#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from typing import List


# @lc code=start
class Solution:

    def partition(self, s: str) -> List[List[str]]:
        comb = []
        palindrome = []

        def check_palindrome():
            nonlocal palindrome
            return palindrome == palindrome[::-1]

        def generate_comb(index):
            nonlocal comb, palindrome

            if index == len(s):
                if check_palindrome():
                    comb.append("".join(palindrome[:]))
                    yield comb[:]
                    comb.pop()
                return

            # if last string is palindrome, we can end it and begin with new character
            if check_palindrome() and palindrome:
                comb.append("".join(palindrome))
                old = palindrome[:]
                palindrome = [s[index]]
                yield from generate_comb(index + 1)
                comb.pop()
                palindrome = old

            # whether or not that last string is palindrome, if last string is not empty, we can append it with new character
            palindrome.append(s[index])
            yield from generate_comb(index + 1)
            palindrome.pop()

        if not s:
            return []

        return list(generate_comb(0))


# @lc code=end
