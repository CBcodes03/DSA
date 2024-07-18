class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new,c=[],0
        for i in nums:
            if i not in new:
                new.append(i)
            else:
                c+=1
                continue
        nums=new+['_' for i in range(c)]
        return (len(nums)-c)