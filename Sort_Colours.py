class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i,ptr=0,0
        while i<=2:
            j=ptr
            while j<len(nums):
                if nums[j] ==i:
                    nums[ptr],nums[j] = nums[j],nums[ptr]
                    ptr+=1
                    j+=1
                else:
                    j+=1
                    continue
            i+=1
        return nums