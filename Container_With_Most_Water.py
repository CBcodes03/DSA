class Solution(object):
    def maxArea(self, height):
        l=0
        m=0
        r=len(height)-1
        while l<r:
            if height[l] < height[r]:
                if height[l]*abs(r-l) > m:
                    m=height[l]*abs(r-l)
                l+=1
            else:
                if height[r]*abs(r-l) > m:
                    m=height[r]*abs(r-l)
                r-=1
        return m
