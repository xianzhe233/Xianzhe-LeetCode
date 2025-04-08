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

        def depth(node):

            if node == None:
                return 0

            left, right = depth(node.left), depth(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return depth(root) != -1


# @lc code=end
