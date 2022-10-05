from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.N, self.M = len(matrix), len(matrix[0])
        self.mat = matrix
        for y in range(self.N):
            for x in range(1, self.M):
                self.mat[y][x] += self.mat[y][x-1]
        
        for y in range(1, self.N):
            for x in range(0, self.M):
                self.mat[y][x] += self.mat[y-1][x]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a, b = min(row2, self.N-1), min(col2, self.M-1)
        answer = self.mat[a][b]
        if row1 - 1 >= 0 and col1 - 1 >= 0: answer += self.mat[row1-1][col1-1]
        if row1 - 1 >= 0: answer -= self.mat[row1-1][b]
        if col1 - 1 >= 0: answer -= self.mat[a][col1-1]
        return answer

