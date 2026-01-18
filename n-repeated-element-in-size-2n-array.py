class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i] +=1
                if d[i] > 1:
                    return i
            else:
                d[i]=1
