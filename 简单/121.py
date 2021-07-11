class Solution:
    def maxProfit(self, prices):
        buy_price=prices[0]
        res=0
        for i in prices:
            if i <buy_price:
                buy_price=i
            else:
                res=max(res,i-buy_price)
        return res
if __name__ == '__main__':
    pirces=[7,1,5,3,6,4]
    so=Solution()
    print(so.maxProfit(pirces))