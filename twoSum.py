def twoSum(nums,target):
    n = len(nums)
    index = {}
    for i in range(0,n):
        index[nums[i]] = i

    for i in range(0,n):
        other = target - nums[i]
        if other in index and index[other] != i:
            return (i,index[other])
    return (-1,-1)

def twoSumOrder(nums,target):
    n = len(nums)
    left,right = 0,n-1
    while left<right:
        # print(left)
        if nums[left] + nums[right] == target:
            return (left,right)
        elif nums[left] + nums[right] < target:
            left = left + 1
        elif nums[left] + nums[right] > target:
            right = right - 1
    return (-1,-1)
if __name__ == '__main__':
    a = [i for i in range(0,10)]
    print(twoSum(a,6))
    print(a)
    print(twoSumOrder(a,6))