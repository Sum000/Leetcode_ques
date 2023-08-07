class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        
        l = 0
        h = n
        
        while (l <= h):
            m = l + ((h - l) // 2)
            
            if m**2 + m - 2*n < 0:
                l = m + 1
                res = m
            elif m**2 + m - 2*n > 0:
                h = m - 1
            else:
                return m
        return res
            
            
                