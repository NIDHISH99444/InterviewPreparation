from heapq import heappop,heappush


nums = [1]
k = 1


def checkFreq(nums,k):
    freqArr={}
    for ele in nums:
        if ele not in freqArr:
            freqArr[ele]=1
        else:
            freqArr[ele]+=1
    heap=[]
    for key,val in freqArr.items():

        heappush(heap,(val,key))
        if k>0:
            k-=1
        else:
            heappop(heap)
    res=[]
    while heap:
        res.append(heappop(heap)[1])
    return res
print(checkFreq(nums,k))