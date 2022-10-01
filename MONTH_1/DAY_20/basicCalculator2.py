class Solution:
    def calculate(self, s: str) -> int:
        s = "".join(s.split())
        def getNumber(x):
            y = x+1
            while y < len(s) and s[y].isdigit():
                y += 1
            return int(s[x:y]), y

        i = 0
        temp = None
        result = 0
        sign = 1
        while i < len(s):
            if s[i].isdigit():
                temp, i = getNumber(i)
                while i < len(s) and (s[i] == '/' or s[i] == '*'):
                    if i < len(s) and s[i] == '/':
                        next, i = getNumber(i+1)
                        temp /= next
                        temp = int(temp)
                    elif i < len(s) and s[i] == '*':
                        next, i = getNumber(i+1)
                        temp *= next
                result += temp*sign
            elif s[i] == '+':
                sign = 1
                i += 1
            elif s[i] == '-':
                sign = -1
                i += 1
        return result 
            


sol = Solution()
equ = '1+4*2*2+2*2'
print(sol.calculate(equ))