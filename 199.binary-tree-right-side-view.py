#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)

        while q:
            right_val = None

            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    right_val = node.val
                    q.append(node.left)
                    q.append(node.right)

            if right_val != None:
                res.append(right_val)

        return res


# @lc code=end
