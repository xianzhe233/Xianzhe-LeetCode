#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
from collections import deque
from typing import Optional


# @lc code=start
# Definition for a Node.
class Node:

    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        q.append(root)

        while q:
            last = None

            for _ in range(len(q)):
                node = q.popleft()

                if node == None:
                    continue

                q.append(node.left)
                q.append(node.right)

                # if `last` is a node, let last.next be current node
                if last:
                    last.next = node

                last = node

            # last node points at None
            if last:
                last.next = None

        return root


# @lc code=end
