class Solution:
    def isPalindrome(self, s:str):
        if s=='':
            return True
        res=''.join(ans.lower() for ans in s if ans.isalnum())
        rev_res=res[::-1]
        if rev_res==res:
            return True
        return False
if __name__ == '__main__':
    string='hello, word1'
    res = ''.join(ans for ans in string if ans.isalnum())
    print(res)
    rev_res=res[::-1]
    print(rev_res)