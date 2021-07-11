class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        hashtable={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        sum = 0
        for i in range(len(s) - 1):
            sum = sum + hashtable[s[i]]
            if hashtable[s[i]] < hashtable[s[i + 1]]:
                sum = sum - 2 * hashtable[s[i]]
        sum = sum + hashtable[s[-1]]
        return sum
if __name__ == '__main__':
    hashtable = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    s="L"
    sum=0

    for i in range(len(s)-1):
        sum=sum+hashtable[s[i]]
        if hashtable[s[i]]<hashtable[s[i+1]]:
            sum=sum-2*hashtable[s[i]]
    sum=sum+hashtable[s[-1]]
    print(sum)


