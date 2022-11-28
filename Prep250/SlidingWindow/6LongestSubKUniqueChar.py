

def longestSubString(arr,k):
    i,j=0,0
    maxVal=0
    map={}
    while j<len(arr):
        if arr[j] not in map:
            map[arr[j]]=1
        else:
            map[arr[j]]+=1
        if len(map)==k:
            maxVal=max(maxVal,j-i+1)
        elif len(map)>k:
            while len(map)>k:
                map[arr[i]]-=1
                if map[arr[i]]==0:
                    del map[arr[i]]
                i+=1
        j+=1
    return maxVal




arr="aabbcc"
k = 2
print(longestSubString(arr,k))