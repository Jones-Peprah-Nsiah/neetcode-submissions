class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        q=deque([])
        dist=0
        visited=set()

        def add_rooms(r,c):
            if((r<0 or r>=rows or
               (c<0 or c>=cols) or
               (r,c) in visited) or
               (grid[r][c]==-1)):
               return

            visited.add((r,c))
            q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
                    visited.add((r,c))

        

        while q:
            for i in range(len(q)):
                (r,c)=q.popleft()
                grid[r][c]=dist
                add_rooms(r-1,c)
                add_rooms(r+1,c)
                add_rooms(r,c-1)
                add_rooms(r,c+1)

            dist+=1

            """
            I would use multi-source BFS because we need to find the shortest distance from each land cell to its nearest treasure.
First, I'll create a queue and a visited set. I'll scan the entire grid and add all treasure cells, represented by 0, to the queue. This allows me to start BFS from all treasures simultaneously.
Next, I'll process the queue level by level. For each cell, I'll assign its current distance and explore its four neighbors: up, down, left, and right.
Before adding a neighbor to the queue, I'll check that it's within the grid, isn't water, and hasn't already been visited.
After processing all cells at the current level, I'll increment the distance by one.
BFS guarantees the shortest distance because it explores cells in increasing order of distance from the treasures.
The time complexity is O(m × n) because each cell is visited at most once. The space complexity is also O(m × n) because of the queue and visited set.
            """


       