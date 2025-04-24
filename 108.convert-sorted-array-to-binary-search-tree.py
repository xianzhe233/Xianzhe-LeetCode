#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
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

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        root_index = len(nums) // 2
        root_val = nums[root_index]
        left_nums = nums[:root_index]
        right_nums = nums[root_index + 1:]

        return TreeNode(root_val, self.sortedArrayToBST(left_nums),
                        self.sortedArrayToBST(right_nums))


# @lc code=end
