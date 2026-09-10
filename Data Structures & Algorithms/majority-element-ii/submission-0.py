class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)

        count={}

        for num in nums:
            count[num]=count.get(num,0)+1
        
        for num in count:
            if count[num]>n//3:
                res.append(num)
        return res

        
        