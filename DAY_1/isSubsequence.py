# cleaner solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = t_index = 0
        while t_index < len(t) and s_index < len(s):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        
        if s_index == len(s):
            return True
        else:
            return False

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if len(s) > len(t):
#             return False
#         if len(s) == 0:
#             return True
        
#         s_index = 0
#         for t_index, t_elem in enumerate(t):
#             if s_index == len(s):
#                 return True
#             if t_elem == s[s_index]:
#                 s_index += 1

#         if s_index == len(s):
#             return True
#         else:
#             return False

s = "abc"
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s,t))