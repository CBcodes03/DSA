#https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d={}
        op=0
        for i in nums:
            if (k-i) in d and d[k-i]>0:
                op+=1
                d[k-i]-=1
            else:
                d[i] = d.get(i, 0) + 1
        return op
