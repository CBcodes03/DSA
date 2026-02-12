class Solution:
    '''
      problem:- https://leetcode.com/problems/intersection-of-two-arrays/
    '''
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        d={}
        for i in nums1:
            d[i]=1
        for j in nums2:
            if j in d:
                d[j]+=1
        return [key for key in d.keys() if d[key]>=2]
