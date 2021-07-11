class Solution:
    def majorityElement(self, nums) -> int:
        list=sorted(nums)
        return list[len(nums)//2]
if __name__ == '__main__':
    so=Solution()
    list=[2,2,1,1,1,2,2]
    re=so.majorityElement(list)
    print(re)