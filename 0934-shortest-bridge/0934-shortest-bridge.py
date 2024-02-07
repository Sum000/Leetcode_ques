class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        visit = set()
        
        def invalid(r, c):
            return r < 0 or c < 0 or r == n or c == n
            
        def dfs(r, c):
            if (invalid(r, c) or grid[r][c] == 0 or (r, c) in visit):
                return 
            
            visit.add((r, c))
            
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                dfs(row, col)
                
        
        def bfs():
            res, q = 0, deque(visit)
            
            while q:
                for i in range(len(q)):
                    
                    r, c = q.popleft()
                    
                    for dr, dc in directions:
                        ROW = r + dr
                        COL = c + dc
                        if (invalid(ROW, COL) or (ROW, COL) in visit):
                            continue
                        
                        if grid[ROW][COL]:
                            return res
                        
                        visit.add((ROW, COL))
                        q.append([ROW, COL])
                        
                res += 1
                
            
            
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)
                    return bfs()