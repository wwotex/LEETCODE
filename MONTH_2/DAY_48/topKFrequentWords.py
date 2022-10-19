from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = [x[::-1] for x in Counter(words).items()]
        words.sort(key = lambda x: (-x[0], x[1]) )
        return [el[1] for el in words][:k]

sol = Solution()
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 3
print(sol.topKFrequent(words, k))