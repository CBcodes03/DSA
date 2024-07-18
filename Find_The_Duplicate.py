class Solution(object):
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
        seen=list(seen)
        return seen[0]
