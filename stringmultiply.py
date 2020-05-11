def multiply(num1,num2):
    m = len(num1)
    n = len(num2)
    res = [0] * (m + n)
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            mul = int(num1[i]) * int(num2[j])
            p1 = i + j
            p2 = i + j + 1
            summ = mul + res[p2]
            res[p2] = summ%10
            res[p1] += int(summ/10)
    print(res)

    i = 0
    while i < len(res) and res[i] == 0:
        i = i + 1

    string = []
    for i in range(0,len(res)):
        string.append(str(res[i]))

    return string if len(string) > 0 else '0'

if __name__ == '__main__':
    # nums = [i for i in range(10,0,-1)]
    # print(nums)
    # print(subarraysum(nums,9))
    num1 = '12'
    num2 = '32'
    result = multiply(num1,num2)
    print(result)