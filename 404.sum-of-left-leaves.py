#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
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

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def is_leaf(node):
            return not node.left and not node.right

        def traversal(node, is_left=False):
            if not node:
                return 0

            if is_leaf(node):
                if is_left:
                    return node.val
                return 0
            else:
                return traversal(node.left, is_left=True) + traversal(
                    node.right, is_left=False)

        sum = traversal(root)

        return sum


# @lc code=end
