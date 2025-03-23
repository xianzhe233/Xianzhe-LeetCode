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
        if root == None:
            return []

        return [root.val] + self.preorderTraversal(
            root.left) + self.preorderTraversal(root.right)


# @lc code=end
