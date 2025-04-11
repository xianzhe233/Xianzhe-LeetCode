#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
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

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = -1
        q = deque()
        q.append(root)

        while q:
            skip = False

            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    q.append(node.left)
                    q.append(node.right)

                    if skip:
                        continue
                    else:
                        ans = node.val
                        skip = True

        return ans


# @lc code=end
