#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#
from typing import List


# @lc code=start
class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        num_5 = 0
        num_10 = 0

        # num_20 is actually useless
        # num_20 = 0

        def change(cash):
            nonlocal num_5, num_10
            # nonlocal num_20

            if cash == 5:
                # for $5, just receive them
                num_5 += 1
            elif cash == 10:
                # for $10, the only way to give change is returning $5

                # there must be at least one $5
                assert num_5 >= 1

                num_10 += 1
                num_5 -= 1
            elif cash == 20:
                # for $20, there are 2 ways to give change:
                # 1. 3 x $5
                # 2. $5 + $10
                # since $5 is always needed, always try to consume $10 first
                # actually, $20 is always useless

                assert (num_5 >= 3) or (num_5 >= 1 and num_10 >= 1)

                if num_5 >= 1 and num_10 >= 1:
                    num_5 -= 1
                    num_10 -= 1
                    # num_20 += 1
                else:
                    num_5 -= 3
                    # num_20 += 1

        for bill in bills:
            try:
                change(bill)
            except:
                return False

        return True


# @lc code=end
