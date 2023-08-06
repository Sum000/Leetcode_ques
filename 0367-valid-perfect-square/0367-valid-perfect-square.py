class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        while low <= high:
            mid = low + (high - low) // 2
            if mid**2 < num:
                low = mid + 1
            elif mid**2 > num:
                high = mid - 1
            else:
                return True
        return False
             
                