#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
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

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def get_inorder_list():
            res = []

            def traversal(node):
                if not node:
                    return

                traversal(node.left)
                res.append(node.val)
                traversal(node.right)

            traversal(root)

            return res

        inorder = get_inorder_list()

        return min(
            [inorder[i] - inorder[i - 1] for i in range(1, len(inorder))])


# @lc code=end
