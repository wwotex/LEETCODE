from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = [[0 for x in range(len(grid[0]))] for y in range(len(grid)) ]
        self.grid = grid
        self.max_x = len(grid)
        self.max_y = len(grid[0])
        islands = 0
        
        for i in range(self.max_x):
            for j in range(self.max_y):
                if self.isReachable(i,j):
                    islands += 1
                    self.visitTile(i,j)

        return islands

    def visitTile(self,x,y):
        self.visited[x][y] = 1
        
        if self.isReachable(x+1,y): self.visitTile(x+1,y)
        if self.isReachable(x-1,y): self.visitTile(x-1,y)
        if self.isReachable(x,y+1): self.visitTile(x,y+1)
        if self.isReachable(x,y-1): self.visitTile(x,y-1)
    
    def isReachable(self, x, y):
        return 0 <= x < self.max_x and 0 <= y < self.max_y and not self.visited[x][y] and self.grid[x][y] == '1'