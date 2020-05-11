def intervalIntersection(A,B):
    i,j = 0,0
    res = []
    while i < len(A) and j < len(B):
        a1,a2 = A[i][0], A[i][1]
        b1,b2 = B[j][0], B[j][1]

        if b2 >= a1 and a2 >= b1:
            res.append([max(a1,b1),min(a2,b2)])
        if b2 < a2:
            j = j + 1
        else:
            i = i + 1
    return res

if __name__ == '__main__':
    A = [[1,3],[4,8]]
    B = [[1,2],[5,9]]
    res = intervalIntersection(A,B)
    print(res)
    # a = [[1,2]]
    # b = a[-1]
    # b[1] = 100
    # print(a)
