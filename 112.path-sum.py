#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def is_leaf(node):
            return not node.left and not node.right

        def traversal(node, path_sum):
            if not node:
                return False

            path_sum += node.val

            if is_leaf(node):
                return path_sum == targetSum
            else:
                return traversal(node.left, path_sum) or traversal(
                    node.right, path_sum)

        return traversal(root, 0)


# @lc code=end
