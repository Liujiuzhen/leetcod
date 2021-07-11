class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={
            '(':')',
            '[':']',
            '{':'}'
        }
        list=[]
        if len(s)%2!=0:
            return False
        for char in s :
            if char in hashmap.keys():
                list.append(char)
            else:
                if len(list)==0:
                    return False
                pop_char=hashmap.get(list.pop())
                if pop_char!=char:
                    return False

        return not list
if __name__ == '__main__':
    so=Solution()
    s='[]'
    flag=so.isValid(s)
    print(flag)