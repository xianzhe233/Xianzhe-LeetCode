#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#
from typing import List

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # add one zero line and zero column at index 0
        # to deal with special conditions
        self.sums = [[0] * (len(matrix[0]) + 1)] + [[0] + line for line in matrix]

        self.height = len(self.sums)
        self.width = len(self.sums[0])

        for i in range(1, self.height):
            for j in range(1, self.width):
                self.sums[i][j] += self.sums[i-1][j] + self.sums[i][j-1] - self.sums[i-1][j-1]

    @staticmethod
    def translate(*coordinates):
        return list(map(lambda x: x + 1, coordinates))

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Adjust coordinates to be 1-indexed to match the 'sums' matrix
        row1, col1, row2, col2 = NumMatrix.translate(row1, col1, row2, col2)
        return self.sums[row2][col2] - self.sums[row2][col1 - 1] - self.sums[row1 - 1][col2] + self.sums[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
obj.sumRegion(1, 2, 3, 4)
