class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            if target-nums[i] not in d:
                d[nums[i]] = i
            else:
                return [i,d[(target-nums[i])]]
        return []
