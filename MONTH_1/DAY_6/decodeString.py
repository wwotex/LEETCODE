class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        self.s = f'1[{s}]'
        return self.expand(0)[0]
    
    def expand(self, start):
        result = []
        num, i = self.findNum(start)
        
        while self.s[i] != ']':
            if self.s[i].isdigit():
                expanded, index = self.expand(i)
                result.append(expanded)
                i = index
            else:
                result.append(self.s[i])
            i += 1
        
        result = ''.join([''.join(result) for x in range(num)])

        return result, i
    
    def findNum(self, start):
        num = []
        i = start
        while self.s[i].isdigit():
            num.append(self.s[i])
            i += 1
        num = int(''.join(num))
        i += 1
        return num, i

sol = Solution()
s = "2[abc]3[cd]ef"
print(sol.decodeString(s))