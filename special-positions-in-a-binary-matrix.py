#url:- https://leetcode.com/problems/special-positions-in-a-binary-matrix/
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        c=0
        row_count=[sum(row) for row in mat]
        col_count=[]
        m=len(mat)
        n=len(mat[0])
        for row in range(m):
            if sum(mat[row]) == 1:
                for col in range(n):
                    if mat[row][col] ==1:
                        if sum(mat[i][col] for i in range(m)) == 1:
                            c+=1
        return c
