class Solution:
    def findMinDiff(self, A,N,M):
        if M==0 or N==0:
            return 0
        A.sort()
        if N < M:
            return -1
        min_diff = float('inf')
        for i in range(N - M + 1):
            diff = A[i + M - 1] - A[i]
            if diff < min_diff:
                min_diff = diff
        
        return min_diff
