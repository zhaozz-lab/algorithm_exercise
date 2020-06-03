def missingnumber(nums):
    res = 0
    n = len(nums)
    res ^= n
    for i in range(n):
        res ^=i^nums[i]
    return res

if __name__ == '__main__':
    b = [0,3,1,4]
    print(missingnumber(b))