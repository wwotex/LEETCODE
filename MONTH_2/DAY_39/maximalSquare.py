from typing import List


class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        N, M = len(mat), len(mat[0])
        size = 0
        for y in range(N):
            for x in range(M):
                mat[y][x] = int(mat[y][x])
                if x > 0: mat[y][x] += mat[y][x-1]
        
        for y in range(1, N):
            for x in range(0, M):
                mat[y][x] += mat[y-1][x]
        
        def isSquare(y, x):
            answer = mat[y+size][x+size]
            if y > 0 and x > 0: answer += mat[y-1][x-1]
            if y > 0: answer -= mat[y-1][x+size]
            if x > 0: answer -= mat[y+size][x-1]
            return answer == (size+1)**2
        
        for y in range(N):
            if y+size >= N: break
            for x in range(M):
                if x+size >= M: break
                while x+size < M and y+size < N and isSquare(y, x):
                    size += 1

        return size**2

sol = Solution()
matrix = [["0","1"],["1","0"]]
print(sol.maximalSquare(matrix))
