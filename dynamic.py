def coinChange(coins,amount:int):
    def dp(n):
        if n==0: return 0
        if n<0: return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n-coin)
            # 子问题无解，则跳过
            if subproblem == -1:
                continue
            res = min(res,1+subproblem)
        return res if res!=float('INF') else -1
    return dp(amount)
# print(coinChange([1,2,5],40))
 
def coinChange(coins,amount):
    memo = dict()
    def dp(n):
        if n-1 in memo: return memo[n-1]
        if n==0: return 0
        if n<0: return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n-coin)
            if subproblem ==  -1: continue
            res = min(res,1+subproblem)
        memo[n] = res if res!=float('INF') else -1
        return memo[n]
    return dp(amount)
print(coinChange([1,2,5],40))

def coinChange(coins,amount):
    dp = [amount+1]*(amount+1)
    dp[0] = 0
    for i in range(0,amount+1):
        for coin in coins:
            if i -coin < 0:
                continue
            dp[i] = min(dp[i],1+dp[i-coin])
    return -1 if dp[amount]==amount+1 else dp[amount]
print(coinChange([1,2,5],40))

res = []
def permute(nums):
    track = []
    backtrack(nums,track)
    return res

def backtrack(nums1,track):
    nums = nums1.copy()
    if len(track) == len(nums):
        res.append(track)
        # track = []
        return
    for i in range(0,len(nums)):
        if nums[i] in track:
            continue
        track.append(nums[i])
        nums.remove(nums[i])
        backtrack(nums,track)
        track = track[:-1]
print(permute([1,2,3]))

