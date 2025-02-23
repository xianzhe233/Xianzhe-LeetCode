#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
from typing import List

# @lc code=start
class Solution:
    INF = 1e10
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def length(start, end):
            return end - start + 1
        
        minLength = Solution.INF
        start = 0
        end = 0
        sum = nums[0]
        
        while not (sum < target and end == len(nums) - 1):
            while sum < target and end < len(nums) - 1:
                end += 1
                sum += nums[end]
            while sum >= target and start <= end:
                minLength = min(minLength, length(start, end))   
                sum -= nums[start]
                start += 1
        
        if minLength == Solution.INF:
            return 0
        return minLength
# @lc code=end

Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3])