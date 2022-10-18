class Solution:
    def countAndSay(self, n: int) -> str:
        k = 1
        curr = '1'
        while k < n:
            cnt = 0
            new = ''
            for i, dig in enumerate(curr):
                cnt += 1
                if i + 1 >= len(curr) or curr[i+1] != dig:
                    new += str(cnt) + dig
                    cnt = 0
            curr = new
                    
            k += 1
        return curr

sol = Solution()
n = 30

print(sol.countAndSay(n))