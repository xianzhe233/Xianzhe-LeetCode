#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
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

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pre_sum = 0

        def traversal(root):
            nonlocal pre_sum

            if not root:
                return

            traversal(root.right)

            pre_sum += root.val
            root.val = pre_sum

            traversal(root.left)

        traversal(root)

        return root


# @lc code=end
