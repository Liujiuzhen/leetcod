class Solution:
    def climbStairs(self, n: int) -> int:
        f1=1
        f2=2
        res=0
        if n==1:
            return 1
        if n==2:
            return 2
        for i in range(3,n+1):
            res=f1+f2
            f1=f2
            f2=res
        return res
if __name__ == '__main__':
    so=Solution()
    re=so.climbStairs(4)
    print(re)