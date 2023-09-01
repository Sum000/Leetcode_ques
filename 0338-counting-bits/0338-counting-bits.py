class Solution:
    def countBits(self, n: int) -> List[int]:
        li = [0] * (n + 1)
        
        for i in range(1, n + 1):
            li[i] = li[i >> 1] + (i & 1)
            
        return li
        