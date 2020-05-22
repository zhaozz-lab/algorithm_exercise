def canFinish(piles,speed,H):
    time = 0
    for n in piles:
        time += timeOf(n,speed)
    return time<=H


def timeOf(n,speed):
    remainder = 1 if n%speed>0 else 0
    return int(n/speed) + remainder


def min_eating_speed(piles,H):
    maxspeed = max(piles)
    for speed in range(1,maxspeed):
        if canFinish(piles,speed,H):
            return speed
    return maxspeed


def min_eating_speed_binary_search(piles,H):
    maxspeed = max(piles)
    left,right = 1,maxspeed
    while left < right:
        mid = left + int((right - left)/2)
        if canFinish(piles,mid,H):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    piles = [3,6,7,11]
    H = 8
    print(min_eating_speed(piles,H))
    print(min_eating_speed_binary_search(piles,H))
