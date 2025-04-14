#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#
from typing import List, Optional

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def build(l, r):
            """
            Returns a TreeNode with MBT structure.
            Args:
                l: left index of `nums`, included
                r: right index of `nums`, excluded
            """
            if l == r:
                return None

            sub_nums = nums[l:r]
            maximum = max(sub_nums)
            max_index = nums.index(maximum)

            return TreeNode(maximum, build(l, max_index),
                            build(max_index + 1, r))

        return build(0, len(nums))


# @lc code=end
