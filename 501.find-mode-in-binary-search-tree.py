#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#
from typing import List, Optional


# @lc code=start
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        current_cnt = 1
        last_node = None
        max_cnt = 0
        res = []

        def traversal(node):
            if not node:
                return

            # use variables outside
            nonlocal current_cnt, last_node, max_cnt, res

            # left subtree
            traversal(node.left)

            # current node
            if not last_node:
                pass
            elif last_node.val == node.val:
                current_cnt += 1
            else:
                current_cnt = 1

            if current_cnt > max_cnt:
                max_cnt = current_cnt
                res.clear()
                res.append(node.val)
            elif current_cnt == max_cnt:
                res.append(node.val)

            # current node become next nodes' last_node
            last_node = node

            # right subtree
            traversal(node.right)

        traversal(root)

        return res


# @lc code=end
