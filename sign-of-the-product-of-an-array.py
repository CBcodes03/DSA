class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            if x==0:
                return 0
            if x < 0:
                return -1
            if x > 0:
                return 1
        product=1
        for i in nums:
            product*=signFunc(i)
        return signFunc(product)
