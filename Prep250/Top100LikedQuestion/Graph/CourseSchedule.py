from collections import defaultdict
def canFinish( n, prerequisites):
    dct = defaultdict(list)
    for ele in prerequisites:
        dct[ele[0]].append(ele[1])

    print(dct)
    indegree = [0] * n
    for val in dct.values():
        for v in val:
            indegree[v] += 1
    print(indegree)
    q = []
    for index,ele in enumerate(indegree):
        if ele == 0:
            q.append(index)
    res = []
    while q:
        ele = q.pop(0)
        res.append(ele)
        for val in dct[ele]:
            indegree[val] -= 1
            if indegree[val] == 0:
                q.append(val)
    print("res",res)

    if len(res)==n:
        return True
    return False

n=20
prerequisites=[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
print(canFinish(n,prerequisites))