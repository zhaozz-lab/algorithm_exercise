def removeDuplicates(nums):
    slow,fast = 0,1
    n = len(nums)
    while fast < n:
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    return slow + 1

if __name__ == '__main__':
    nums = [1,2,3,3,3,4]
    print(removeDuplicates(nums))