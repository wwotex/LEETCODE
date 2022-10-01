from collections import deque

class Solution:
    def orangesRotting(self, grid):
        self.grid = grid
        Q = deque()
        self.fresh_oranges = 0
        self.pushRotten(Q)
        Q.append((-1,-1)) # add delimiter between timesteps
        timesteps = -1

        while Q:
            temp = Q.popleft()
            if temp[0] == -1:
                timesteps += 1
                if Q: Q.append((-1,-1))

            self.addAdjacents(temp, Q)
            
        return timesteps if self.fresh_oranges == 0 else -1
                

    def addAdjacents(self, cell, queue):
        a, b = cell[0], cell[1]
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        for el in directions:
            new_a, new_b = a + el[0], b + el[1]  
            self.rottenIfFresh((new_a, new_b), queue)
        
    def rottenIfFresh(self, cell, queue):
        a, b = cell[0], cell[1]
        if 0 <= a < len(self.grid) and 0 <= b < len(self.grid[0]) and self.grid[a][b] == 1:
            self.grid[a][b] = 2
            self.fresh_oranges -= 1
            queue.append((a,b))

    def pushRotten(self, queue):
        for i, row in enumerate(self.grid):
            for j, el in enumerate(row):
                if el == 2:
                    queue.append((i,j))
                elif el == 1:
                    self.fresh_oranges += 1

sol = Solution()
grid = [[1],[2]]
print(sol.orangesRotting(grid))