class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        charset=set()
        l=0
        for r in range(len(nums)):
            if r-l>k:
               charset.remove(nums[l])
               l+=1

            
            if nums[r] in charset:
                return True

            charset.add(nums[r])
        return False
                

           
