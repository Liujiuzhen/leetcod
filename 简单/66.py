class Solution:
    def plusOne(self, digits) :
        digits=[str(i) for i in digits]
        num=int(''.join(digits))
        num+=1
        str_num=str(num)
        str_list=list(str_num)
        num_list=[int(i) for i in str_list]
        return num_list


        pass

if __name__ == '__main__':
    a = [1,2,3,4,5]
    a = [str(i) for i in a]
    b = int(''.join(a))
    print(b)
    b=str(b)
    b=list(b)
    print(b)
