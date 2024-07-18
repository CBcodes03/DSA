class Solution(object):
    def findDuplicates(self, nums):
        seen = set()
        duplicates = set()
        for num in nums:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        return list(duplicates)
            
