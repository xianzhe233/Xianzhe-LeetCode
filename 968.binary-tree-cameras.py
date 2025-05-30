#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
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

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        CAMERA = 0
        MONITORED = 1
        UNCOVERED = 2

        ans = 0

        def traversal(root):
            nonlocal ans

            # empty root
            if not root:
                return MONITORED

            left = traversal(root.left)
            right = traversal(root.right)

            if left == MONITORED and right == MONITORED:
                return UNCOVERED
            elif left == UNCOVERED or right == UNCOVERED:
                ans += 1
                return CAMERA
            # left == CAMERA or right == CAMERA
            else:
                return MONITORED

        root_state = traversal(root)

        if root_state == UNCOVERED:
            ans += 1

        return ans


# @lc code=end
