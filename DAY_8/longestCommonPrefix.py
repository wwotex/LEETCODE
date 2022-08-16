class Solution:
    def longestCommonPrefix(self, strs):
        result = []
        i = s = 0
        n_str = len(strs)
        min_len_str = 201
        for el in strs:
            min_len_str = min(min_len_str, len(el))
        while i < min_len_str:
            if s == 0:
                result.append(strs[s][i])
            elif result[i] != strs[s][i]:
                result.pop()
                break

            s+=1
            if s == n_str:
                s = 0
                i += 1

        return "".join(result)

sol = Solution()
strs = ["flower","flow","flight"]
print(sol.longestCommonPrefix(strs))