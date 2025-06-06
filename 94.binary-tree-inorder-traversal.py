#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
from typing import Optional, List


# @lc code=start
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if node == None:
                continue

            if visited:
                res.append(node.val)
                continue

            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))

        return res


# @lc code=end
