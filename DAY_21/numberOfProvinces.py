from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        prov = 1
        prov_table = [0 for x in range(n)]

        for city in range(n):
            if prov_table[city] == 0:
                S = [city]
                while S:
                    curr_city = S.pop()
                    prov_table[curr_city] = prov
                    for neigh, connection in enumerate(isConnected[curr_city]):
                        if connection and prov_table[neigh] == 0:
                            S.append(neigh)
                prov += 1
        
        return prov-1

sol = Solution()
isConnected = [[1,0],[0,1]]
print(sol.findCircleNum(isConnected))