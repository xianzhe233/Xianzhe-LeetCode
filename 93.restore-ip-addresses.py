#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
from typing import List


# @lc code=start
class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:

        def check_length(rest_part, rest_length):
            # for every rest part, 1 is the shortest length, 3 is the longest length
            # if rest length do not in [1 * rest_part, 3 * rest_part], this combination cannot be valid
            return rest_part * 1 <= rest_length <= rest_part * 3

        def check_number(num_string):
            return (str(int(num_string))
                    == num_string) and (0 <= int(num_string) <= 255)

        comb = []
        integer_string = ""

        def generate_ip(index):
            nonlocal comb, integer_string

            def rest_part():
                return 4 - len(comb)

            def rest_length():
                return len(s) - index

            # base case
            if rest_length() == 0:
                # during the process, every integer part will checked to be valid, so no rest digit implies valid partition
                if rest_part() == 1 and check_number(integer_string):
                    yield ".".join(comb + [integer_string])

                # unused digits is left, not valid partition
                return

            # pruning: if rest length is impossible to get valid partition, stop this path
            if not check_length(rest_part(),
                                rest_length() + len(integer_string)):
                return

            # if it's valid to append current integer with this char, try to append it
            if check_number(integer_string + s[index]):
                integer_string += s[index]
                yield from generate_ip(index + 1)
                integer_string = integer_string[:-1]

            # end current integer, and begin a new one
            # assume current integer is always valid
            # one single digit (0-9) is always valid
            if integer_string:
                old = integer_string[:]
                comb.append(integer_string)
                integer_string = s[index]
                yield from generate_ip(index + 1)
                comb.pop()
                integer_string = old

        if not check_length(4, len(s)):
            return []

        return list(generate_ip(0))


# @lc code=end
test = Solution()
print(test.restoreIpAddresses("25525511135"))
