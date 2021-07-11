class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashtable={}
        for i,num in enumerate(nums):
            if target-num in hashtable.keys():
                return [hashtable[target-num],i]
            else:
                hashtable[num]=i
        return []
if __name__ == '__main__':
    so=Solution()
    nums = [1, 2, 3, 4, 5]
    re=so.twoSum(nums,10)
    print(re)

