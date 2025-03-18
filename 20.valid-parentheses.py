#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


class Solution:

    def isValid(self, s: str) -> bool:
        parentheses = []
        lefts = ('(', '[', '{')
        rights = (')', ']', '}')
        for c in s:
            if c in lefts:
                parentheses.append(c)
            else:
                index = rights.index(c)
                try:
                    last = parentheses.pop()
                except IndexError:
                    return False
                if last != lefts[index]:
                    return False

        return len(parentheses) == 0


# @lc code=end
