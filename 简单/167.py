class Solution:
    def twoSum(self, numbers, target: int):
        result=[]
        i=0
        j=len(numbers)-1
        while i<j:

            if numbers[i]+numbers[j]>target:
                j=j-1
            elif numbers[i]+numbers[j]<target:
                i=i+1
            else:
                result.append(i+1)
                result.append(j+1)
                break
        return result
if __name__ == '__main__':
    so=Solution()
    numbers = [3,24,50,79,88,150,345]
    target = 200
    re=so.twoSum(numbers,target)
    print(re)
