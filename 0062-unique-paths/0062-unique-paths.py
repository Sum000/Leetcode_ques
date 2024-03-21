class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        zero = []
        for i in range(m):
            for j in range(n):
                zero.append(0)
            dp.append(zero)
            
        dp[m - 1][n - 1] = 1
                
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                top = dp[i][j + 1] if j + 1 < n else 0
                down = dp[i + 1][j] if i + 1 < m else 0
                dp[i][j] = top + down
                
        return dp[0][0]
               
                
                    
        