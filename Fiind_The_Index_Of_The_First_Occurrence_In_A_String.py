class Solution(object):
    def strStr(self, haystack, needle):
        w=len(needle)-1
        for i in range(len(haystack)-w):
            if haystack[i:i+w+1] == needle:
                return i
        return -1
