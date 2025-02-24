#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
from typing import List

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = list(list(0 for i in range(n)) for j in range(n))

        def verify(x, y):
            return x >= 0 and y >= 0 and x < n and y < n and A[x][y] == 0
        
        def printMatrix():
            for i in range(n):
                for j in range(n):
                    print(A[i][j], end=" ")
                print("")
        
        dx = (0, 1, 0, -1)
        dy = (1, 0, -1, 0)
        x, y = 0, 0
        mod = 0
        index = 0
        
        while index < n ** 2:
            index += 1
            A[x][y] = index
            nx, ny = x + dx[mod], y + dy[mod]
            if not verify(nx, ny):
                mod = (mod + 1) % 4
            x, y = x + dx[mod], y + dy[mod]
        
        # printMatrix()
        return A

# @lc code=end
Solution().generateMatrix(3)