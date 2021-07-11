class Solution:
    def generate(self, numRows: int):
        re_list=[]
        list_start=[1]
        if numRows==0:
            return re_list
        re_list=[[1]]
        if numRows==1:
            return re_list
        for i in range(1,numRows):
            list_tmp=[]
            list_right=re_list[i-1].copy()
            list_left=re_list[i-1].copy()
            list_right.append(0)
            list_left.insert(0,0)
            for j in range(0,len(list_right)):
                list_tmp.append(list_right[j]+list_left[j])
            re_list.append(list_tmp)
        return re_list
if __name__ == '__main__':
    so=Solution()
    re=so.generate(3)
    print(re)
    # list=[[1]]
    # list[0].append(0)
    # print(type(list))