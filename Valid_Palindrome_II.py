class Solution(object):
    def validPalindrome(self, s):
        def helper(string):
            if string[::-1] == string:
                return True
            else:
                False
        if helper(s):
            return True
        else:
            i=0
            j=len(s)-1
            while i<j:
                if s[i] != s[j]:
                    if helper(s[:i]+s[i+1:]):
                        return True
                    elif helper(s[:j]+s[j+1:]):
                        return True
                    else:
                        return False
                else:
                    i+=1
                    j-=1
                    continue
