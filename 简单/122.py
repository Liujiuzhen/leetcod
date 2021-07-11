class Solution:
    def maxProfit(self, prices):
        res=0
        for i in range(len(prices)-1):
            if prices[i+1]-prices[i]>0:
                res=res+prices[i+1]-prices[i]
        return res
if __name__ == '__main__':
    so=Solution()
    lists=[7,1,5,3,6,4]
    print(so.maxProfit(lists))