class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        
        if n == 0:
            return [0]
        
        li = []
        li.append(0)
        li.append(1)
        
        for i in range(2, n + 1):
            li.append(li[i >> 1] + i % 2)
            
        return li
        