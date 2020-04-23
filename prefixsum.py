def subarraysum(nums,target):
    sums = []
    sums.append(0)
    for i in range(1,len(nums)):
        sums.append(sums[i-1] + nums[i])
    ans = 0
    for j in range(0,len(nums)):
        for k in range(0,j):
            if sums[j] -  sums[k] == target:
                ans += 1
    return ans

def subarraysum(nums,target):
    sums = {}
    sums[0] = 1
 
    ans = 0
    nums_sum = 0
    for i in range(0,len(nums)):
        nums_sum += nums[i]
        if nums_sum - target in sums:
            ans += 1
        if nums_sum in sums:
            sums[nums_sum] += 1
        else:
            sums[nums_sum] = 1

    return ans
if __name__ == '__main__':
    nums = [i for i in range(0,10)]
    print(subarraysum(nums,9))
