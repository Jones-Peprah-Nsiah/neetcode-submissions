class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=[-s for s in stones]

        heapq.heapify(maxheap)
        while len(maxheap)>1:


            first=heapq.heappop(maxheap)
            second=heapq.heappop(maxheap)

            if first !=second:
                heapq.heappush(maxheap, -abs(second-first))

        return -maxheap[0] if maxheap else 0

        