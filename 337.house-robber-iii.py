#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
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

    def rob(self, root: Optional[TreeNode]) -> int:

        def robber(root: Optional[TreeNode]):
            """
            Returns a int pair (dp[False], dp[True])
            """

            # empty node
            if not root:
                return (0, 0)

            dp_l = robber(root.left)
            dp_r = robber(root.right)

            # do not rob this house
            dp_F = max(dp_l) + max(dp_r)
            # rob this house, left and right can't be robbed
            dp_T = dp_l[0] + dp_r[0] + root.val

            return dp_F, dp_T

        return max(robber(root))


# @lc code=end
