class Solution(object):
    def longestCommonPrefix(self, strs):
        s=strs[0]
        f=True
        for i in range(len(s)):
            for j in strs:
                if len(j)==i or j[i] != s[i]:
                    return(s[:i])
        return s
