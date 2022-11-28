
def subarrayOfSumK( arr, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    i , j =0 ,0
    sum ,cnt =0 ,0
    if len(arr )==1:
        if arr[0 ]==k:
            return 1
        else:
            return 0

    while j< len(arr):
        sum += arr[j]
        # if sum < k:
        #     j+=1
        if sum == k:
            cnt += 1
            # j+=1
        elif sum > k:
            while sum > k:
                sum -= arr[i]
                i += 1
            if sum == k:
                cnt += 1
        j += 1
    return cnt


arr=[-1,-1,1]
k=0

print(subarrayOfSumK(arr,k))