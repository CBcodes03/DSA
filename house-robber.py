class Solution:
    '''
      problem-url:- https://leetcode.com/problems/house-robber/
    '''
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n <= 2:
            return max(nums)
        dp=nums[:]
        dp[1] = max(dp[:2])
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i]+dp[i-2])
        return dp[n-1]
