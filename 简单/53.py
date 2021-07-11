import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start=0
        maxre=nums[0]
        for i in nums:
            pre=max(i,start+i)
            maxre=max(maxre,pre)
        return maxre

