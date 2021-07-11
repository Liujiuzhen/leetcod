class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=False
        if x<0:
            x=-x
            flag=True
        sum=0
        while x>10:
            y=x%10
            x=x//10
            sum=sum*10+y
        sum=sum*10+x
        if flag:
            if sum>=2**31:
                return 0
            else:
                return -sum
        if sum >= 2 ** 31 - 1:
            return 0
        else:
            return sum
if __name__ == '__main__':
    x=10
    sum=0
    while x>=10:
        y=x%10
        x=x//10
        sum=sum*10+y
    print(sum*10+x)
