class Solution(object):
    from collections import deque
    def findMaxValueOfEquation(self, points, k):
        dq = deque()
        max_value = float('-inf')
        for x, y in points:
            while dq and x - dq[0][1] > k:
                dq.popleft()
            if dq:
                max_value = max(max_value, dq[0][0] + y + x)
            while dq and dq[-1][0] <= y - x:
                dq.pop()
            dq.append((y - x, x))
        
        return max_value
