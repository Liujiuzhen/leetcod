class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        sum = 0
        re_x=x
        while x > 10:
            y = x % 10
            x = x // 10
            sum = sum * 10 + y
        sum = sum * 10 + x
        if sum==re_x:
            return True
if __name__ == '__main__':
    so=Solution()
    print(so.isPalindrome(121))