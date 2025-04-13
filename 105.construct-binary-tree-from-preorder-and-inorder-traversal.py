#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
from typing import List, Optional


# @lc code=start
# Definition for a binary tree node.
# comment TreeNode when submit
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]

        if len(inorder) == len(preorder) == 1:
            return TreeNode(root_val, None, None)

        inorder_root_index = inorder.index(root_val)
        left_sub_inorder = inorder[:inorder_root_index]
        right_sub_inorder = inorder[inorder_root_index + 1:]
        left_len, right_len = len(left_sub_inorder), len(right_sub_inorder)
        left_sub_preorder = preorder[1:left_len + 1]
        right_sub_preorder = preorder[-right_len:]

        return TreeNode(root_val,
                        self.buildTree(left_sub_preorder, left_sub_inorder),
                        self.buildTree(right_sub_preorder, right_sub_inorder))


# @lc code=end
