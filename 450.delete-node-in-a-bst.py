#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
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

    def deleteNode(self, root: Optional[TreeNode],
                   key: int) -> Optional[TreeNode]:

        def find_successor_of(root: TreeNode):

            def find_minimum(root: Optional[TreeNode]):
                if not root:
                    return root

                current = root

                while current.left:
                    current = current.left

                return current

            return find_minimum(root.right)

        if not root:
            return None

        if root.val == key:
            if not root.left and not root.right:
                return None
            elif root.left and root.right:
                successor = find_successor_of(root)
                self.deleteNode(root, successor.val)
                root.val = successor.val

                return root
            else:
                return root.left if root.left else root.right

        else:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            else:
                root.right = self.deleteNode(root.right, key)

            return root


# @lc code=end
