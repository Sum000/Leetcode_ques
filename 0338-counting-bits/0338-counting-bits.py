class Solution:
    def countBits(self, n: int) -> List[int]:
        li = []
        if n == 0:
            return [0]
        
        li.append(0)
        
        for i in range(1, n + 1, 1):
            no_ones = bin(i).count("1")
            li.append(no_ones)
            
        return li
    
    
    
    
        