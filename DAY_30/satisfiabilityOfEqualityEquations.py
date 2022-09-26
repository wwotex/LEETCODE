from collections import defaultdict
from tkinter import E
from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        inequalities = []
        equalities = {}
        def find(el):
            if el not in equalities: equalities[el] = el
            if equalities[el] == el:
                return el
            else:
                return find(equalities[el])
        
        def union(el1, el2):
            p1, p2 = find(el1), find(el2)
            equalities[p1] = p2

        for eq in equations:
            if eq[0] == eq[3] and eq[1] == '!': return False

            key1, key2 = eq[0], eq[3]
            equal = 1 if eq[1] == '=' else 0
            
            if equal:
                union(key1, key2)
            else:
                inequalities.append((key1, key2))
        
        for (el1, el2) in inequalities:
            if find(el1) == find(el2):
                return False

            
        return True

sol = Solution()
eq = ["c==c","b==d","x!=z"]
print(sol.equationsPossible(eq))