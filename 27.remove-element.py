#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        it1, it2 = 0, 0
        while True:
            while it1 < len(nums) and nums[it1] != val:
                it1 += 1
            if it1 == len(nums):
                break
            
            if it2 == 0:
                it2 = it1 + 1
            while it2 < len(nums) and nums[it2] == val:
                it2 += 1
            if it2 == len(nums):
                break
            
            nums[it1], nums[it2] = nums[it2], nums[it1]

        count = 0
        for num in nums:
            if num != val:
                count += 1
        return count




# @lc code=end

