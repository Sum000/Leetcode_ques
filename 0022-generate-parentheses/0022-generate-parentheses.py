class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(openB, closedB, currstr):
            if openB == closedB == 0:
                res.append(currstr)
                return 
            
            elif closedB < openB or openB < 0 or openB > n:
                return 
            
            backtrack(openB - 1, closedB, currstr + "(")
            backtrack(openB, closedB - 1, currstr + ")")
            
            
        backtrack(n, n, "")
        return res
        