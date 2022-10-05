from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        for y in range(1, height):
            for x in range(len(triangle[y])):
                if x-1 < 0: 
                    triangle[y][x] += triangle[y-1][x]
                elif x >= len(triangle[y-1]):
                    triangle[y][x] += triangle[y-1][x-1]
                else:
                    triangle[y][x] += min( triangle[y-1][x-1], triangle[y-1][x] )
        return min(triangle[-1])