from typing import List


class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        for y in range(len(mat)):
            for x in range(len(mat[0])):
                mat[y][x] = int(mat[y][x])
                if mat[y][x] == 1 and y-1 >= 0 and x-1 >= 0:
                    mat[y][x] = min(mat[y-1][x], mat[y][x-1], mat[y-1][x-1]) + 1

        return max([max(el) for el in mat])**2

sol = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(sol.maximalSquare(matrix))