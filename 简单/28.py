class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if str=='':
            return 0
        re=haystack.find(needle)
        return re

if __name__ == '__main__':
    str='abc'
    re=str.find('bcd')
    print(re)