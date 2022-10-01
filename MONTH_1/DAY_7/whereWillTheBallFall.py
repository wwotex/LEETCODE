class Solution:
    def findBall(self, grid):
        lenx, leny = len(grid), len(grid[0])
        def exists(a,b):
            return 0 <= a <= lenx and 0 <= b < leny
        def propagate(a,b,top):
            if a == lenx:
                return b
            if not top:
                return propagate(a+1, b, top=True)
            if grid[a][b] == 1 and exists(a, b+1) and grid[a][b+1] == 1:
                return propagate(a, b+1, top=False)
            if grid[a][b] == -1 and exists(a, b-1) and grid[a][b-1] == -1:
                return propagate(a, b-1, top=False)

            return -1
            
        result = []    
        for ball in range(leny):
            result.append(propagate(0, ball, top=True))
        return result

sol = Solution()
grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
print(sol.findBall(grid))