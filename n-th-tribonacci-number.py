class Solution:
    '''
      problem-url:- https://leetcode.com/problems/n-th-tribonacci-number/
    '''
    def tribonacci(self, n: int) -> int:
        if n==0:
            return n
        if n==1 or n==2:
            return 1
        t,t1,t2=0,1,1
        for i in range(3,n+1):
            temp=t+t1+t2
            t=t1
            t1=t2
            t2=temp
        return t2
