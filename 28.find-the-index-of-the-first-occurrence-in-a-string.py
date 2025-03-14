#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#


# @lc code=start
class Solution:

    def strStr(self, haystack: str, needle: str) -> int:

        def build_next(pattern):
            next = [0]
            L = 0
            i = 1

            while i < len(pattern):
                if pattern[i] == pattern[L]:
                    L += 1
                    next.append(L)
                    i += 1
                else:
                    if L == 0:
                        next.append(L)
                        i += 1
                    else:
                        L = next[L - 1]

            return next

        next = build_next(needle)
        i, j = 0, 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            elif j > 0:
                j = next[j - 1]
            else:
                i += 1

            if j == len(needle):
                return i - j

        return -1


# @lc code=end
