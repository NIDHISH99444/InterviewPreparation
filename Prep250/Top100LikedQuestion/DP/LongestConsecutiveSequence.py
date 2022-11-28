


def maxSequence(arr):
    set_arr=set(arr)
    maxVal=0
    for ele in set_arr.copy():
        x=ele-1
        if x not in set_arr:
            y=ele+1
            while y in  set_arr:
                y+=1
            maxVal=max(maxVal,y-x-1)

    return maxVal


arr=[100]
print(maxSequence(arr))