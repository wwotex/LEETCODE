from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.visited = [[0 for x in range(len(image[0]))] for y in range(len(image)) ]
        self.image = image
        self.max_x = len(image)
        self.max_y = len(image[0])
        self.color = color
        self.init_color = image[sr][sc]
        self.fillTile(sr,sc)
        return self.image

    def fillTile(self,x,y):
        self.visited[x][y] = 1
        self.image[x][y] = self.color
        
        if self.isReachable(x+1,y): self.fillTile(x+1,y)
        if self.isReachable(x-1,y): self.fillTile(x-1,y)
        if self.isReachable(x,y+1): self.fillTile(x,y+1)
        if self.isReachable(x,y-1): self.fillTile(x,y-1)
    
    def isReachable(self, x, y):
        return 0 <= x < self.max_x and 0 <= y < self.max_y and not self.visited[x][y] and self.image[x][y] == self.init_color

sol = Solution()
im = [[0,0,0],[0,0,0]]
x, y = 0, 0
color = 0
print(sol.floodFill(im, x, y, color))