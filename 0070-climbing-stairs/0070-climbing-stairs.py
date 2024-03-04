class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        
        def backtrack(total):
            if total >= n:
                return 1 if total == n else 0
            
            if total in dp:
                return dp[total]
            
            dp[total] = backtrack(total + 1) + backtrack(total + 2)
            
            return dp[total]
        
        
        return backtrack(0)
        