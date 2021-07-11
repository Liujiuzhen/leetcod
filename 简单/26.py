class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        n=len(nums)
        fast=1
        slow=1
        while fast<n:
            if nums[fast]!=nums[fast-1]:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow

if __name__ == '__main__':
    nums=[1,2,3,4,5]
    for i in range(0,len(nums)):
        nums[i]=nums[4-i]
    print(nums)