#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#
from collections import deque
from typing import List, Optional

# @lc code=start
# Definition for a binary tree node.
INF = float('inf')


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)

        while q:
            maximum = -INF

            for _ in range(len(q)):
                node = q.popleft()

                if node != None:
                    maximum = max(maximum, node.val)
                    q.append(node.left)
                    q.append(node.right)

            if maximum != -INF:
                res.append(maximum)

        return res


# @lc code=end
