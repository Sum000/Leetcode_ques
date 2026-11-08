class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        # brute force appraoch. Time: O(mn(m + n)), space: O(1)
        # res = 0
        # m, n = len(grid), len(grid[0])
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:

        #             row_count = 0
        #             for col in range(n):
        #                 if grid[i][col] == 1:
        #                     row_count += 1

        #             col_count = 0
        #             for row in range(m):
        #                 if grid[row][j] == 1:
        #                     col_count += 1

        #             if row_count > 1 or col_count > 1:
        #                 res += 1

        # return res
                    

        # optimized solution
        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        res += 1

        return res


        

                            


        