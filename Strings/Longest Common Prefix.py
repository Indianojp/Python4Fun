class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        for i in range(0,len(strs[0])):
            for x in strs:
                if len(x)-1 < i:
                    return res
                if strs[0][i] not in x[i]:
                    return res
            res += strs[0][i]
        return res