#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start


class Solution:

    def numTrees(self, n: int) -> int:
        # num_bst[x]: num of distinct BSTs with `x` nodes
        num_bst = [0] * (n + 1)

        # initialization: there's only 1 unique BST for 0 node (empty BST) and 1 unique BST for 1 node (just that node)
        num_bst[0] = num_bst[1] = 1

        for num_node in range(2, n + 1):
            # num_left: number of nodes of left subtree
            # num_right: number of nodes of right subtree
            # num_left + num_right = num_node - 1 (because root consumes one node)
            for num_left in range(0, n):
                num_right = (num_node - 1) - num_left

                # left-right subtree combinations
                num_bst[num_node] += num_bst[num_left] * num_bst[num_right]

        return num_bst[n]


# @lc code=end
Solution().numTrees(4)
