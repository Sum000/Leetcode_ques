class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(i, cur):
            if len(cur) == k:
                res.append(cur.copy())
                return 
            
            for num in range(i, n + 1):
                cur.append(num)
                backtrack(num + 1, cur)
                
                cur.pop()
                
                
        backtrack(1, [])
        return res
                
                
        