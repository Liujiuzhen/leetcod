class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length=len(nums)
        if length==0:
            return 0
        if nums[-1]==target:
            return length-1
        if nums[-1]<target:
            return length
        if nums[0]>=target:
            return 0
        for i in range(0,length):
            if nums[i]==target:
                return i
            if nums[i]<target and nums[i+1]>target:
                return i+1





        pass
