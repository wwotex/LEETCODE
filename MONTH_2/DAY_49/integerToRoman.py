class Solution:
    def intToRoman(self, num: int) -> str:
        N = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        S = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        ptr = len(N)-1
        result = ''
        while num > 0:
            while num < N[ptr]:
                ptr -= 1
            num -= N[ptr]
            result += S[ptr]
        return result


sol = Solution()
print(sol.intToRoman(3999))
# for num in range(1, 30):
#     print(sol.intToRoman(num))