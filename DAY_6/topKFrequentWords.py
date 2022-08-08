from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        D = {}
        for el in words:
            if el in D:
                D[el] += 1
            else:
                D[el] = 0
        
        D = list(D.items())
        D.sort(key=lambda y: (-y[1], y[0]))
        result = []
        for i, el in enumerate(D):
            if i >= k:
                break
            result.append(el[0])
        return result
        
sol = Solution()

words = ["i","love","leetcode","i","love","coding"]
k = 3
print(sol.topKFrequent(words, k))
        