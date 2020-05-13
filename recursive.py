
nums = [0]*6
def merge(nums,lo,mid,hi):
    i,j = lo,mid+1
    aux = nums.copy()
    
    for k in range(lo,hi+1):
        if i > mid:
            nums[k] = aux[j]
            j += 1
        elif j > hi:
            nums[k] = aux[i]
            i += 1
        elif aux[i] >= aux[j]:
            nums[k] = aux[i]
            i += 1
        else:
            nums[k] = aux[j]
            j += 1
    print(nums)
    return nums


def sort(nums,lo,hi):
    if lo >= hi:
        return
    mid = lo + int((hi - lo)/2)
    sort(nums,lo,mid)
    sort(nums,mid+1,hi)
    nums = merge(nums,lo,mid,hi)
    return nums


def mergesort(nums):
    # n = len(nums)
    # lo,hi = 0,n-1
    return sort(nums,0,len(nums)-1)

if __name__ == '__main__':
    nums = [1,2,6,8,5,7]
    print(mergesort(nums))

    
                   