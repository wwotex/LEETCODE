class Solution:
    def spiralOrder(self, matrix):
        x = y = 0
        lenx, leny = len(matrix), len(matrix[0])
        def exists(a,b):
            return 0 <= a < lenx and 0 <= b < leny and matrix[a][b] != 101
        result = []
        direction = 0
        changed_direction = False
        while x >= 0:
            if matrix[x][y] != 101:
                result.append(matrix[x][y])
            matrix[x][y] = 101
            newx, newy = x, y
            if direction == 0:
                newy += 1
            elif direction == 1:
                newx += 1
            elif direction == 2:
                newy -= 1
            else:
                newx -= 1
            
            if exists(newx, newy):
                x = newx
                y = newy
                changed_direction = False
            elif changed_direction:
                break
            else:
                direction = (direction+1)%4
                changed_direction = True


        return result
            
sol = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(sol.spiralOrder(matrix))