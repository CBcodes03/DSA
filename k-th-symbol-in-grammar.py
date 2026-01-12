class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        prev = self.kthGrammar(n-1,(k+1)//2)
        if k%2==1:
            return prev
        elif k%2!=1:
            return 1-prev
