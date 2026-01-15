class Solution:
    "url:- https://leetcode.com/problems/rotate-image/"
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #we transpose and reverse:
        n=len(matrix[0])
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            matrix[i] = matrix[i][::-1]
        return None
