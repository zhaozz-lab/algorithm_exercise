def maxEnvelopes(envelopes):
    n = len(envelopes)
    envelopes.sort(key = lambda env:env[0])
    # height = [0] * n
    height = [envelopes[i][1] for i in range(0,n)]

    return lengthofLIS(height)


def lengthofLIS(nums):
    piles,n = 0,len(nums)
    top = [0]*n
    for i in range(0,n):
        poker = nums[i]
        left,right = 0,piles
        while left < right:
            mid = int((left + right)/2)
            if top[mid] >= poker:
                right = mid

            else:
                left = mid + 1
        if left == piles:
            piles += 1
        top[left] = poker
    return piles

if __name__ == '__main__':
    envelopes = [[1,2],[2,3],[1,3],[4,6]]
    envelop = maxEnvelopes(envelopes)
    print(envelop)

