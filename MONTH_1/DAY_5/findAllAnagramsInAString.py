from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answers = []
        dick = {}
        dick_comp = {}
        for el in p: 
            if el in dick:
                dick[el] += 1
            else:
                dick[el] = 1
                dick_comp[el] = 0
        
        

        len_p = len(p)
        letters_covered = 0
        for i, el in enumerate(s):
            if i >= len_p and s[i-len_p] in dick:
                dick_comp[s[i-len_p]] -= 1
                if dick_comp[s[i-len_p]] < dick[s[i-len_p]]:
                    letters_covered -= 1
            if el in dick:
                dick_comp[el] += 1
                if dick_comp[el] <= dick[el]:
                    letters_covered += 1
            if letters_covered == len_p:
                answers.append(i-len_p+1)
        
        return answers

sol = Solution()
s = "cbaebabacd"
p = "abc"
print(sol.findAnagrams(s, p))