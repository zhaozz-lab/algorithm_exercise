def missingnumber(nums):
    res = 0
    n = len(nums)
    res ^= n
    for i in range(n):
        res ^=i^nums[i]
    return res

def find_error_numbers(nums):
    n = len(nums)
    dup = -1
    for i in range(0,n):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            dup = abs(nums[i])
        else:
            nums[index] *= -1

    missing = -1
    for i in range(0,n):
        if nums[i] > 0:
            missing = i + 1
    
    return missing,dup

if __name__ == '__main__':
    b = [0,3,1,4]
    print(missingnumber(b))
    c = [0,1,2,2,3]
    print(find_error_numbers(c))