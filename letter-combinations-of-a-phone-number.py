class Solution:
    '''
      problem:- https://leetcode.com/problems/letter-combinations-of-a-phone-number/
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        d={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        n=len(digits)
        res=[]
        if n==0:
            return res
        def helper(idx:int,curr:str)->None:
            if len(curr) == n:
                res.append(curr)
                return None
            for i in d[digits[idx]]:
                helper(idx+1,curr+i)
        helper(0,"")
        return res
