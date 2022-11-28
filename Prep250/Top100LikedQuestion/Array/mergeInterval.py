

def merge( intervals):
    res = []
    intervals.sort()
    print(intervals)
    res.append(intervals[0])
    for i in range(1, len(intervals)):
        first = intervals[i]
        if res[-1][1] >= first[0]:
            left, right = res.pop()
            res.append([left, max(right, first[1])])
            print(res)
        else:
            print(res)
            res.append(first)
    return (res)





intervals=[[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]

print(merge(intervals))
