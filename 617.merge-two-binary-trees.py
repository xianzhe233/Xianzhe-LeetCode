#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#
from typing import Optional

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def mergeTrees(self, root1: Optional[TreeNode],
                   root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        if root1 and root2:
            val = root1.val + root2.val
            return TreeNode(val, self.mergeTrees(root1.left, root2.left),
                            self.mergeTrees(root1.right, root2.right))

        return root1 if root1 else root2


# @lc code=end
