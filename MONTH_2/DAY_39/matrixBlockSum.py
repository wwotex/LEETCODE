from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        N, M = len(mat), len(mat[0])
        for y in range(N):
            for x in range(1, M):
                mat[y][x] += mat[y][x-1]
        
        for y in range(1, N):
            for x in range(0, M):
                mat[y][x] += mat[y-1][x]
        
        answer = [[0 for a in range(M)] for b in range(N)]
        for y in range(N):
            for x in range(M):
                a, b = min(y+k, N-1), min(x+k, M-1)
                answer[y][x] = mat[a][b]
                if y - k - 1 >= 0 and x - k - 1 >= 0: answer[y][x] += mat[y-k-1][x-k-1]
                if y - k - 1 >= 0: answer[y][x] -= mat[y-k-1][b]
                if x - k - 1 >= 0: answer[y][x] -= mat[a][x-k-1]
        return answer
                
                

# class Solution:
#     def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
#         N, M = len(mat), len(mat[0])
#         answer = [[0 for x in range(M)] for y in range(N+1)]
#         a = b = 0
#         while a <= k-1 and a < N:
#             b = 0
#             while b <= k and b < M:
#                 answer[0][0] += mat[a][b]
#                 b += 1
#             a += 1
        
#         for y in range(1,N+1):
#             for x in range(M):
#                 up, down, left, right = max(0, y-1-k), min(N-1, y-1+k), max(0, x-k), min(M-1, x+k)
#                 if x == 0:
#                     answer[y][x] = answer[y-1][x]
#                     if y + k < N+1:
#                         answer[y][x] += sum(mat[down][left:right+1])
#                     if up - 1 >= 0:
#                         answer[y][x] -= sum(mat[up-1][left:right+1])
#                 else:
#                     answer[y][x] = answer[y][x-1]
#                     if x + k < M:
#                         answer[y][x] += sum([mat[el][right] for el in range(up, down+1)])
#                     if x - k - 1 >= 0:
#                         answer[y][x] -= sum([mat[el][left-1] for el in range(up, down+1)])
#         return answer[1:]

sol = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(sol.matrixBlockSum(mat, k))