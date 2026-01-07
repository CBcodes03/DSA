class Solution:
  '''
  problem url:- https://leetcode.com/problems/integer-to-roman/
  '''
  def intToRoman(self, num: int) -> str:
        v=[1000, 900, 500, 400,
            100,  90,  50,  40,
            10,   9,   5,   4,
            1]
        r=["M","CM","D","CD",
            "C","XC","L","XL",
            "X","IX","V","IV",
            "I"]
        res=''
        for i in range(len(v)):
            while num >=v[i]:
                num-=v[i]
                res+=r[i]
        return res
