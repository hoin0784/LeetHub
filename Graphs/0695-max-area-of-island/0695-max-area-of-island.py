class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])

        maxAreaOfIsland = 0

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0

            Areas = 1

            Areas += dfs(r + 1, c)
            Areas += dfs(r - 1, c)
            Areas += dfs(r, c + 1)
            Areas += dfs(r, c - 1)

            return Areas

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    maxAreaOfIsland = max(maxAreaOfIsland,dfs(r,c))

        return maxAreaOfIsland

        