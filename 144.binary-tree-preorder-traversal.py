#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()

            if node != None:
                res.append(node.val)
            else:
                continue

            stack.extend([node.right, node.left])

        return res


# @lc code=end
