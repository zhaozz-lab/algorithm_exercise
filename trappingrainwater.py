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
        l_max[i] = max()

    


if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,1,2]]
    image1 = floodFill(image,1,1,3)
    print(image1)