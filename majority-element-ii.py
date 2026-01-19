class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        res=set()
        n=len(nums)
        if n <=2:
            return list(set(nums))
        for i in nums:
            d[i] = d.get(i,0)+1
            if d[i] > n//3:
                res.add(i)
        return list(res)
