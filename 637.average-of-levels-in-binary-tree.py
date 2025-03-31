#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
from collections import deque
from typing import List, Optional


# @lc code=start
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque()
        q.append(root)

        while q:
            total = 0
            length = 0

            for _ in range(len(q)):
                node = q.popleft()

                if node != None:
                    length += 1
                    total += node.val
                    q.append(node.left)
                    q.append(node.right)

            if length:
                res.append(total / length)

        return res


# @lc code=end
