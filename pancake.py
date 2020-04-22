res = []
def pancakesort(cakes):
    sort(cakes,len(cakes))
    return res

def sort(cakes,n): 
    if n==1:
        return
    maxCake = 0
    maxCakeIndex = 0
    for i in range(0,n):
        if cakes[i] > maxCake:
            maxCakeIndex = i
            maxCake = cakes[i]

    # 第一次翻转，最大饼翻到最上边
    reverse(cakes,0,maxCakeIndex)
    res.append(maxCakeIndex+1)
    # 第二次翻转，将最大饼翻到最下边
    reverse(cakes,0,n-1)
    res.append(n)
    # 递归调用
    sort(cakes,n-1)

def reverse(arr,i,j):
    while i<j:
        # temp = arr[i]
        arr[i],arr[j] = arr[j],arr[i]
        # arr[j] = temp
        i = i + 1
        j = j - 1
    print(arr)

if __name__ == '__main__':
    cakes = [2,4,1,0,3]
    pancakesort(cakes)
    print(cakes)