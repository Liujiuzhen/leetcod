class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(' ')
        for i in x[::-1]:
            if i != '':
                return len(i)
        return 0






if __name__ == '__main__':
    s="a"
    so =Solution()
    re=so.lengthOfLastWord(s)
    print(re)


