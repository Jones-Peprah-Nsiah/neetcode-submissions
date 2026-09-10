class Solution:
    def maxDifference(self, s: str) -> int:
        count={}
        largest_odd=a1=0
        smallest_even=float('inf')

        for c in s:
            count[c]=count.get(c,0)+1
        
        for c in s:
            if count[c]%2==0:
                a2=count[c]
                smallest_even=min(a2,smallest_even)

            else:
                a1=count[c]
                largest_odd=max(a1,largest_odd)
        res=largest_odd-smallest_even
        return res

        
        