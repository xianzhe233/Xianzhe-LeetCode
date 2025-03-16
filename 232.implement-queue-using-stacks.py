#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
from contextlib import nullcontext


class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack_in.append(x)
        self.size += 1

    def in_to_out(self):
        """
        Puts all items in stack_in to stack_out.
        """
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

    def pop(self) -> int:
        if not self.stack_out:
            self.in_to_out()
        self.size -= 1
        return self.stack_out.pop()

    def peek(self) -> int:
        item = self.pop()
        self.stack_out.append(item)
        self.size += 1
        return item

    def empty(self) -> bool:
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
