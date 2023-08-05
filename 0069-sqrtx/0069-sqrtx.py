class Solution:
    def mySqrt(self, x: int) -> int:
        low , high = 0, x
        res = 0
        
        while low <= high:
            mid = low + ((high - low) // 2)
            if mid**2 > x:
                high = mid - 1
            elif mid**2 < x:
                low = mid + 1
                res = mid
            else:
                return mid
        return res