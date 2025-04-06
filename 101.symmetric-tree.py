#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def symmetric(a, b):
            if a == None and b == None:
                return True

            if (a == None and b != None) or (a != None and b == None):
                return False

            if a.val != b.val:
                return False

            return symmetric(a.left, b.right) and symmetric(a.right, b.left)

        if root == None:
            return True
        else:
            return symmetric(root.left, root.right)


# @lc code=end
