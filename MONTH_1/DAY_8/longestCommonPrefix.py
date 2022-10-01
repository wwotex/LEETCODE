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

    def longestCommonPrefix2(self, strs):
        result = []

        # unpacks the list into separate strings to zip them so that each character is tupled with the corresponding characters from other strings
        for x in zip(*strs):
            # parse the tuple of characters to a set so that no duplicate elements exist so that if the number of elements is one means all characters were the same
            if len(set(x)) == 1: 
                result.append(x[0])
            else:
                break
        return "".join(result)

sol = Solution()
strs = ["flower","flow","flight"]
print(sol.longestCommonPrefix2(strs))