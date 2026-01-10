class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        f1=True
        f2=True
        #check for ascending
        prev=nums[0]
        for i in range(1,len(nums)):
            if nums[i] >= prev:
                prev = nums[i]
                continue
            else:
                f1=False
                break
        #check for descending
        prev=nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= prev:
                prev = nums[i]
                continue
            else:
                f2=False
                break
        return f1 or f2
