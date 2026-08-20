class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing,duplicate=-1,-1
        seen=set()
        
        for i in range(len(nums)):
            if nums[i] in seen:
                duplicate=nums[i]

            else:
                seen.add(nums[i])

        for i in range(1,len(nums)+1):
            if i not in seen:
                missing=i
        return[duplicate,missing]

        
        