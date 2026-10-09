class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        q=deque([])
        counter=0
        fresh=0
    

        def add_fruit(r,c):
            nonlocal fresh
            if ((r<0 or c<0) or
               (r>=rows or c>=cols) or
               (grid[r][c]==0) or grid[r][c]==2):
               return 

            grid[r][c]=2
            fresh-=1

            q.append((r,c))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))

                elif grid[r][c]==1:
                    fresh+=1


        while q and fresh>0:
            for i in range(len(q)):
                (r,c)=q.popleft()
                add_fruit(r+1,c)
                add_fruit(r-1,c)
                add_fruit(r,c+1)
                add_fruit(r,c-1)
            counter+=1

        
        return counter if fresh==0 else -1



               