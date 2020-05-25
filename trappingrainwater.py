# give a array,judge how much water could be filled
def trap(height):
    n = len(height)
    ans = 0
    for i in range(1,n-1):
        l_max,r_max = 0,0
        for j in range(i,n):
            r_max = max(r_max,height[j])
        for j in range(0,i+1):
            l_max = max(l_max,height[j])

        ans += min(l_max,r_max) - height[i]

    return ans


def trap_memo(height):
    if len(height) < 0:
        return 0
    n = len(height)
    ans = 0 
    l_max,r_max = [0]*n,[0]*n
    l_max[0] = height[0]
    r_max[n-1] = height[n-1]

    for i in range(1,n):
        l_max[i] = max(height[i],l_max[i-1])
    for i in range(n-2,0,-1):
        r_max[i] = max(height[i],r_max[i+1])

    for i in range(1,n-1):
        ans += min(l_max[i],r_max[i]) - height[i]

    return ans

def trap_two_pointer(height):
    n = len(height)
    left,right = 0,n-1
    l_max = height[0]
    r_max = height[n-1]
    ans = 0
    while left <= right:
        l_max = max(l_max,height[left])
        r_max = max(r_max,height[right])
        if l_max < r_max:
            ans += (l_max - height[left])
            left += 1
        else:
            ans += (r_max - height[right])
            right -= 1
    return ans


    


if __name__ == '__main__':
   height = [1,2,3,2,1,0,4]
   print(trap(height))
   print(trap_memo(height))
   print(trap_two_pointer(height))