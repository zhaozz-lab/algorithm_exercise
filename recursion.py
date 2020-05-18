

def sort(nums,test):
    print("2")

def sort(nums):
    print("1")

if __name__ == '__main__':
    # a = [i for i in range(0,10)]
    # print(twoSum(a,6))
    # print(a)
    # print(twoSumOrder(a,6))
    # sort("1")
    sort("1")
    a = [['1','2'],['2','3']]
    print(a)
    b = a[1].copy()
    print(id(b))
    print(id(a[1]))
    b[1] = '10'
    print(a)
    c='1'
    b=c
    b='2'
    print(c)
    print([[0]*10]*10)