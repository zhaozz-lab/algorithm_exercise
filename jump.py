def canjump(nums):
    n = len(nums)
    farthest = 0 
    for i in range(0,n-1):
        farthest = max(farthest,i+nums[i])
        if farthest <= i:
            return False
    return farthest>n-1


# using minist step to result
memo = [] 
def jump(nums):
    n = len(nums)
    memo = [n]*n
    return dp(nums,0,memo)


def dp(nums,p,memo):
    n = len(nums)
    if p > n-1:
        return 0
    # print(p)
    if memo[p] != n:
        return memo[p]
    steps = nums[p]
    for i in range(1,steps + 1):
        subProblem = dp(nums,p + i,memo)
        memo[p] = min(memo[p], subProblem + 1)
    return memo[p]


def jump_greed(nums):
    n = len(nums)
    end,farthest = 0,0
    jumps = 0
    for i in range(0,n):
        farthest = max(nums[i]+i,farthest)
        if end == i:
            jumps += 1
            end = farthest
    return jumps





if __name__ == '__main__':
    a = [1,2,3,6,1,2,3]
    b = [2,1,0,2]
    print(canjump(a))
    print(canjump(b))

    c = [1,2,4,5,2,2,1]
    print(jump(c))
    print(jump_greed(c))