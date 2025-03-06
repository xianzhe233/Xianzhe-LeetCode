#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#


# @lc code=start
class Solution:

    def isHappy(self, n: int) -> bool:
        # digit square sum
        def DSS(num):
            sum = 0
            for c in (str)(num):
                digit = eval(c)
                sum += digit**2
            return sum

        appeared = set([n])
        while n != 1:
            n = DSS(n)
            if n in appeared:
                return False
            else:
                appeared.add(n)

        return True


# @lc code=end
