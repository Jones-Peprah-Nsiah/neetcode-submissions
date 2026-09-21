class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0
        maxheap=[]

        count=Counter(tasks)

        maxheap=[-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        q=deque([])

        while q or maxheap:
            time+=1

            if maxheap:
                cnt=1+heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt,time+n])

            
            if q and q[0][1]==time:
                val=q.popleft()[0]
                heapq.heappush(maxheap,val)

        return time




        