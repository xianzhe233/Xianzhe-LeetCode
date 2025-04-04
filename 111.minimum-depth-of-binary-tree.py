#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
from collections import deque
from typing import Optional


# @lc code=start
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        q = deque()
        q.append(root)

        while q:
            res += 1

            for _ in range(len(q)):
                node = q.popleft()

                if not node.left and not node.right:
                    return res

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return res


# @lc code=end
