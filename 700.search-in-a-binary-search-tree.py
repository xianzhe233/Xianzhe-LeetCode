#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
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

    def searchBST(self, root: Optional[TreeNode],
                  val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right

        return None


# @lc code=end
