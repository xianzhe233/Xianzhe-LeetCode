#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
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

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def is_leaf(node):
            return not node.left and not node.right

        res = []  # answer list

        def traversal(node, path=[]):
            if not node:
                return

            path = path + [str(node.val)]

            if is_leaf(node):
                res.append('->'.join(path))
                return
            else:
                traversal(node.left, path)
                traversal(node.right, path)

        traversal(root)

        return res


# @lc code=end
