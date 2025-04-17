#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(root):
            """
            If this tree is a BST, returns the ([minimum in the tree], [maximum in the tree], True), else return (0, 0, False). `root` CANNOT be None.
            Args:
                root (TreeNode): root of potential BST.
            """
            max_val, min_val = root.val, root.val

            if root.left:
                left_min, left_max, left_valid = validate(root.left)
                max_val = max(max_val, left_max)
                min_val = min(min_val, left_min)

                if not left_valid or left_max >= root.val:
                    return (0, 0, False)

            if root.right:
                right_min, right_max, right_valid = validate(root.right)
                max_val = max(max_val, right_max)
                min_val = min(min_val, right_min)

                if not right_valid or right_min <= root.val:
                    return (0, 0, False)

            return (min_val, max_val, True)

        if not root:
            return True
        else:
            _, _, ans = validate(root)
            return ans


# @lc code=end
