class Solution:
    '''
      problem:-  https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
    '''
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=float('inf')
        for i in range(len(nums)-k+1):
            if abs(nums[i+k-1]-nums[i]) < res:
                res=abs(nums[i+k-1]-nums[i])
        return res
