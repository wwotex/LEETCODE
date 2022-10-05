from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        LEN = len(matrix)
        for y in range(1, LEN):
            for x in range(LEN):
                if x-1 < 0: 
                    matrix[y][x] += min( matrix[y-1][x], matrix[y-1][x+1] )
                elif x+1 >= LEN:
                    matrix[y][x] += min( matrix[y-1][x-1], matrix[y-1][x] )
                else:
                    matrix[y][x] += min( matrix[y-1][x-1], matrix[y-1][x], matrix[y-1][x+1] )
        return min(matrix[-1])

