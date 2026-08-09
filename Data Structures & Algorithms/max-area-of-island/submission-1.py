class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        directions = [[-1,0], [1,0], [0,1], [0,-1]]

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            currentArea = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        print(currentArea, nr , nc)
                        currentArea += 1
                        q.append((nr, nc))
                        visited.add((nr, nc))
            return currentArea

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    currentArea = bfs(r,c)
                    area = max(area, currentArea)

        return area
        