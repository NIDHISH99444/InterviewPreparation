def longestSubstringWithoutRepeatingChar(arr):
    i,j=0,0
    map={}
    maxVal=0
    while j<len(arr):
        if arr[j] not in map:
            map[arr[j]]=1
        else:
            map[arr[j]]+=1
        if len(map)==j-i+1:
            maxVal=max(maxVal,j-i+1)
        elif len(map)<j-i+1:
            while len(map)<j-i+1:
                map[arr[i]]-=1
                if map[arr[i]]==0:
                    del map[arr[i]]
                i+=1
        j+=1
    return maxVal
str="au"
print(longestSubstringWithoutRepeatingChar(str))