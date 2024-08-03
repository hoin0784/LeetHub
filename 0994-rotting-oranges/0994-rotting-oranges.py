class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        days, fresh = 0, 0
        q = deque()
        
        # Initial population of the queue and fresh orange count
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS to spread the rot
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row < 0 or row >= rows or
                        col < 0 or col >= cols or
                        grid[row][col] != 1
                    ):
                        continue
                    
                    # Make it rotten
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            days += 1
        
        return days if fresh == 0 else -1
            
            
                    
                    
                    
        
    
        