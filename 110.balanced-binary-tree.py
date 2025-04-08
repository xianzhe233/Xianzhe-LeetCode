#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
from typing import Optional


# @lc code=start
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth_dict = {}

        def depth(node):

            if node == None:
                return 0

            if node not in depth_dict:
                depth_dict[node] = 1 + max(depth(node.left), depth(node.right))

            return depth_dict[node]

        if root == None:
            return True
        else:
            return self.isBalanced(root.left) and self.isBalanced(
                root.right) and abs(depth(root.left) - depth(root.right)) <= 1


# @lc code=end
