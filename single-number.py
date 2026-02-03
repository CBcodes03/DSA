class Solution:
    '''
      problem_url:- https://leetcode.com/problems/single-number/
    '''
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            res=res^i
        return res
