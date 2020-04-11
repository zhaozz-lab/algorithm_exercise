def binaryresearch(nums,target):
    left,right = 0,len(nums)-1
    while left<=right:
        # print(left)
        mid = left + int((right -left)/2)
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid-1
        elif target > nums[mid]:
            left = mid
    return -1
nums = range(0,19)
print(binaryresearch(nums,20))
a = [1,2,2,3,4,4,5]
print(binaryresearch(a,4))