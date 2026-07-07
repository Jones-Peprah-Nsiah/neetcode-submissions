class Solution:
    def findMin(self, nums: List[int]) -> int:
      minimum=nums[0]

      left,right=0,len(nums)-1
      while left<=right:
         if nums[left]<nums[right]:
            minimum=min(minimum,nums[left])
            break
         m=(left+right)//2

         minimum=min(nums[m],minimum)

         if nums[m]>=nums[left]:
            left=m+1

         else:
            right=m-1

      return minimum



        