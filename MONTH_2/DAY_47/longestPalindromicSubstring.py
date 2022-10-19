import heapq
import numpy as np

class Solution:
    def longestPalindrome(self, s1: str) -> str:
        N = len(s1)
        s2 = s1[::-1]
        dp = [[0 for x in range(N+1)] for y in range(N+1)]
        max_len = 0
        best_palindrome = 0
        for y in range(N, -1, -1): 
            for x in range(N, -1, -1):
                if x == N or y == N:
                    continue
                if s1[y] == s2[x]:
                    dp[y][x] = dp[y+1][x+1] + 1
                    if (N - y - 1) - x + 1 == dp[y][x] and dp[y][x] > max_len:
                        max_len = dp[y][x]
                        best_palindrome = (y, y+dp[y][x])
        return s1[best_palindrome[0]: best_palindrome[1]]

# BRUTE FORCE O(n^3)
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         N = len(s)
#         max_len = 0
#         best_palindrome = ''
#         for left in range(N):
#             for right in range(left+1, N+1):
#                 curr = s[left:right]
#                 if curr == curr[::-1] and right - left > max_len:
#                     max_len = right - left
#                     best_palindrome = curr
#         return best_palindrome


sol = Solution()
s = "twbiqwtafgjbtolwprpdnymaatlbuacrmzzwhkpvuwdtyfjsbsqxrlxxtqkjlpkvpxmlajdmnyepsmczmmfdtjfbyybotpoebilayqzvqztqgddpcgpelwmriwmoeeilpetbxoyktizwcqeeivzgxacuotnlzutdowiudwuqnghjgoeyojikjhlmcsrctvnahnoapmkcrqmwixpbtirkasbyajenknuccojooxfwdeflmxoueasvuovcayisflogtpxtbvcxfmydjupwihnxlpuxxcclbhvutvvshcaikuedhyuksbwwjsnssizoedjkbybwndxpkwcdxaexagazztuiuxphxcedqstahmevkwlayktrubjypzpaiwexkwbxcrqhkpqevhxbyipkmlqmmmogrnexsztsbkvebjgybrolttvnidnntpgvsawgaobycfaaviljsvyuaanguhohsepbthgjyqkicyaxkytshqmtxhilcjxdpcbmvnpippdrpggyohwyswuydyrhczlxyyzregpvxyfwpzvmjuukswcgpenygmnfwdlryobeginxwqjhxtmbpnccwdaylhvtkgjpeyydkxcqarkwvrmwbxeetmhyoudfuuwxcviabkqyhrvxbjmqcqgjjepmalyppymatylhdrazxytixtwwqqqlrcusxyxzymrnryyernrxbgrphsioxrxhmxwzsytmhnosnrpwtphaunprdtbpwapgjjqcnykgspjsxslxztfsuflijbeebwyyowjzpsbjcdabxmxhtweppffglvhfloprfavduzbgkw"
print(sol.longestPalindrome(s))