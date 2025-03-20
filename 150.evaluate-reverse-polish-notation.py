#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
from typing import List

# @lc code=start
import re


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:

        def is_number(s):
            pattern = r"^-?\d+$"
            return bool(re.match(pattern, s))

        stack = []

        def evaluate_and_push(operator):
            """
            Evaluates latest notation and put the result back to stack.
            """

            # the number new pushed into stack is operand2
            operand2 = stack.pop()
            operand1 = stack.pop()

            stack.append(str(int(eval(operand1 + operator + operand2))))

        for token in tokens:
            if is_number(token):
                stack.append(str(token))
            else:
                evaluate_and_push(token)

        return int(stack[0])


# @lc code=end
print(Solution().evalRPN(
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
