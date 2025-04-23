#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
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

    def trimBST(self, root: Optional[TreeNode], low: int,
                high: int) -> Optional[TreeNode]:
        if not root:
            return None

        # if `val` in [low, high], keep `root` and update
        if low <= root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root

        # if `val` > high, `left` is potential valid node
        if root.val > high:
            return self.trimBST(root.left, low, high)
        # if `val` < low, `right` is potential valid node
        else:
            return self.trimBST(root.right, low, high)


# @lc code=end
