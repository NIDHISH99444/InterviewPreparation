
def subarrayOfSumK( arr, k):
    sum=0
    map={}
    j,cnt=0,0
    while j<len(arr):
        sum+=arr[j]
        if sum == k:
            cnt+=1
        elif map.get(sum) is None:
            map[sum]=j
        else:
            cnt+=1
        j+=1
        print(map)
    return cnt




arr=[1,1,1]
k=2

print(subarrayOfSumK(arr,k))