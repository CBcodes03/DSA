class Solution(object):
    import re
    def reverseWords(self, s):
        s=re.sub(r'\s+', ' ', s).strip()
        l=s.split(' ')
        i,j=0,len(l)-1
        while i<=j:
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
        res=''
        for i in l:
            res=res+i+' '
        res=res.strip(' ')
        return res
