#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
from queue import Queue


class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.put(x)

    def turn(self):
        """
        Cycles q until last item becomes front of q.   
        """
        n = self.q.qsize() - 1
        for _ in range(n):
            self.q.put(self.q.get())

    def pop(self) -> int:
        self.turn()
        return self.q.get()

    def top(self) -> int:
        item = self.pop()
        self.q.put(item)
        return item

    def empty(self) -> bool:
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
