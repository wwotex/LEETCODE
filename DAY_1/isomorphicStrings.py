# cleaner approach
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for els, elt in zip(s, t):
            if (elt not in dict_t) and (els not in dict_s):
                dict_s[els] = elt
                dict_t[elt] = els
            elif elt != dict_s.get(els) or els != dict_t.get(elt):
                return False
        return True



# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         dict_s = {}
#         dict_t = {}
#         for i in range(len(s)):
#             if not s[i] in dict_s:
#                 dict_s[s[i]] = t[i]
#             elif t[i] != dict_s[s[i]]:
#                 return False

#             if not t[i] in dict_t:
#                 dict_t[t[i]] = s[i]
#             elif s[i] != dict_t[t[i]]:
#                 return False
#         return True


s = 'badc'
t = 'baba'
sol = Solution()
print(sol.isIsomorphic(s,t))