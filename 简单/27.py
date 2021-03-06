class Solution:
    def removeElement(self, nums: List, val: int) -> int:
        if len(nums) == 0:
            return 0
        slow = 0
        for quick in range(0, len(nums)):
            if nums[quick] != val:
                nums[slow] = nums[quick]
                slow += 1
        return slow



if __name__ == '__main__':
    list=[]
    so=Solution()
    re=so.removeElement(list,3)
    print(re)
