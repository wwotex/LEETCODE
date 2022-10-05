from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if x > 0 and y > 0:
                    grid[y][x] += min(grid[y-1][x], grid[y][x-1])
                elif x > 0:
                    grid[y][x] += grid[y][x-1]
                elif y > 0:
                    grid[y][x] += grid[y-1][x]
        return grid[-1][-1]