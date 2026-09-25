class MedianFinder:

    def __init__(self):
        self.minheap,self.maxheap=[],[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)
        if (self.maxheap and self.minheap and -self.maxheap[0]>self.minheap[0]):
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        if len(self.maxheap)>len(self.minheap)+1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        if len(self.minheap)>len(self.maxheap)+1:
             heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.minheap)>len(self.maxheap):
            return self.minheap[0]

        elif len(self.maxheap)>len(self.minheap):
            return -self.maxheap[0]

        return (-self.maxheap[0] + self.minheap[0])/2
        