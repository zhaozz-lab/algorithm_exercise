def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key = lambda intv:intv[0])
    res = []
    res.append(intervals[0])
    for i in range(1,len(intervals)):
        curr = intervals[i]
        last = res[-1]
        # 如果小于等于，则合并，会默认更新
        if curr[0] <= last[1]:
            last[1] = max(last[1],curr[1])
        else:
            res.append(curr)
    return res
if __name__ == '__main__':
    nums = [[1,2],[2,5],[3,6],[10,12]]
    res = merge(nums)
    print(res)
    a = [[1,2]]
    b = a[-1]
    b[1] = 100
    print(a)
