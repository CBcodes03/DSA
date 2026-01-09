class Solution:
    """
      problem url:- https://leetcode.com/problems/pascals-triangle/
    """
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        if numRows > 1:
            for i in range(1,numRows):
                prev=res[i-1]
                curr=[]
                for j in range(i+1):
                    curr.append((prev[j-1] if j-1>=0 else 0) + (prev[j] if j<len(prev) else 0))
                res.append(curr)
        return res
