from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parents = {} # rows positive and columns negative
        result = 0
        
        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x
        
        def union(x, y):
            parents[y] = x

        for [row, column] in stones:
            row += 1
            column += 1
            if row not in parents and (-column) not in parents:
                parents[row] = row
                parents[-column] = row
                continue

            if row in parents and (-column) in parents:
                s1, s2 = find(row), find(-column)
                if s1 != s2:
                    result += 1
                    union(s1, s2)
            elif row in parents:
                parents[-column] = find(row)
            elif (-column) in parents:
                parents[row] = find(-column)
            
            result += 1 
        return result

sol = Solution()
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
print(sol.removeStones(stones))