#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#


# @lc code=start
class Solution:

    def monotoneIncreasingDigits(self, n: int) -> int:
        n_list = list(map(int, str(n)))
        digit_list = []

        def MID(index, lower_bound, bound_mark=True):
            # base case: find valid answer
            if index == len(n_list):
                return True

            # greedy: if there's no need to smaller than `n_list[index]`, just fill 9
            if not bound_mark:
                digit_list.append(str(9))
                if not MID(index + 1, 9, False):
                    digit_list.pop()
                    return False
                else:
                    return True
            else:
                # for bits that need to be smaller than `n_list[index]`, their range is [lower_bound, n_list[index]]
                for digit in range(n_list[index], lower_bound - 1, -1):
                    digit_list.append(str(digit))
                    # digit == corresponding digit in `n`, following digits should be <=, bound_mark = True
                    if digit == n_list[index]:
                        if not MID(index + 1, digit, True):
                            digit_list.pop()
                        else:
                            return True
                    else:
                        if not MID(index + 1, digit, False):
                            digit_list.pop()
                        else:
                            return True

                # if no digits to use / no digits are valid, return False
                return False

        MID(0, 0)

        return int(''.join(digit_list))


# @lc code=end
