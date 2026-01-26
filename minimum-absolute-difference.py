class Solution:
    '''
      problem:- https://leetcode.com/problems/minimum-absolute-difference/
    '''
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=float('inf')
        result=[]
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1]) < res:
                res=abs(arr[i]-arr[i+1])
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1]) == res:
                result.append([arr[i],arr[i+1]])
        return result
