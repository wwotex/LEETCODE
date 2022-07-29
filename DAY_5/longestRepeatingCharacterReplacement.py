class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_result = 1
        D = {}
        back = front = 0
        D[s[0]] = 1
        while front < len(s):
            win_size = (front - back + 1)
            if (self.max_val(D) + k) < win_size:
                D[s[back]] -= 1
                back += 1
            else:
                longest_result = max(longest_result, win_size)
                front += 1
                if front < len(s):
                    if s[front] in D: 
                        D[s[front]] += 1
                    else:
                        D[s[front]] = 1
        
        return longest_result

    def max_val(self, d):
        return d[ max(d, key=d.get) ]

sol = Solution()
s = "AABABBA"
k = 1
print(sol.characterReplacement(s, k))