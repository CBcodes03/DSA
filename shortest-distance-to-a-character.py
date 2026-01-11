class Solution:
    """
        problem url:- https://leetcode.com/problems/shortest-distance-to-a-character/
    """
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexes=[]
        res=[]
        def helper(i,arr=indexes):
            return min([abs(i-j) for j in indexes])
        for k in range(len(s)):
            if s[k] == c:
                indexes.append(k)
        for i in range(len(s)):
            if s[i] == c:
                res.append(0)
            else:
                res.append(helper(i))
        return res
