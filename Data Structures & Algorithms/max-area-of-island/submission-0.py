class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        rows = len(grid)
        cols = len(grid[0])

        directions = [[-1,0], [1,0], [0,1], [0,-1]]

        def bfs(r, c):
            q = collections.deque()
            visited = set()
            visited.add((r,c))
            q.append((r,c))
            currentArea = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    r = r + dr
                    c = c + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visited:
                        currentArea += 1
                        q.append((r, c))
                        visited.add((r, c))
            return currentArea

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    currentArea = bfs(r,c)
                    area = max(area, currentArea)

        return area
        