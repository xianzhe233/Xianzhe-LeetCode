#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
from collections import deque
from typing import List, Optional


# @lc code=start
# Definition for a Node.
class Node:

    def __init__(self,
                 val: Optional[int] = None,
                 children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)

        while q:
            layer = []

            for _ in range(len(q)):
                node = q.popleft()

                if node == None:
                    continue

                layer.append(node.val)
                for child in node.children:
                    q.append(child)

            if layer:
                res.append(layer)

        return res


# @lc code=end
