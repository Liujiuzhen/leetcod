class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs=sorted(strs,key=lambda i:len(i))
        min_str=strs[0]
        for i in range(len(strs)):
            for j in range(len(min_str)):
                if min_str[j]!=strs[i][j]:
                    min_str=min_str[:j]
                    break


        return min_str


if __name__ == '__main__':
    so=Solution()
    strs = ["flower", "flow", "flight"]
    re=so.longestCommonPrefix(strs)
    print(re)