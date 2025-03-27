#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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

                q.append(node.left)
                q.append(node.right)

            if layer:
                res.append(layer)

        return res


# @lc code=end
