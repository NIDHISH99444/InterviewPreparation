# Pointers to remember
# 1> Adding  list  and string
#     lst =[]
#     str="a"
#     res=lst+[str]
#     Convert string into list and append to list
# 2> Adding 2 string
#     str1=""
#     str2=""
#     str3=str1+str2
# 3> Making shalow copy of  variable using arr[:] when we are updating into final result , otherwise array gets
#     updated in final call


#print all substring

def subset(chosen,remainder):
    if len(remainder) ==0:
        print(chosen)
        return
    subset(chosen+remainder[0],remainder[1:])
    subset(chosen,remainder[1:])
#subset('',"abc")

#returing list without passing res variable

def subsetListReturn(chosen,remainder):
    if len(remainder) ==0:
        res=[]
        res.append(chosen)
        return res
    left=subsetListReturn(chosen+remainder[0],remainder[1:])
    right=subsetListReturn(chosen,remainder[1:])
    left.extend(right)
    return left
#print("subset list ",subsetListReturn('',"abc"))

#sum equal to number in list
# def checksum(chosen,remainder,expectedsum):
#     if not len(remainder) and expectedsum == 0:
#         return 1
#     if not len(remainder) or expectedsum< 0:
#         return 0
#     left = checksum(chosen+[remainder[0]],remainder[1:],expectedsum-remainder[0])
#     right = checksum(chosen,remainder[1:],expectedsum)
#
#     return left + right

def checksum(chosen,remainder,expectedsum):
    if len(remainder)==0:
        res=[]
        if sum(chosen)==expectedsum:
            res.append(chosen)
        return  res
    return checksum(chosen+[remainder[0]],remainder[1:],expectedsum) + checksum(chosen,remainder[1:],expectedsum)
arr=[1,2,1]
expectedsum=2
#print(f"Printing all sum {checksum([],arr,expectedsum)}")

#print first some equal to given sum

def printFirstsum(chosen,remainder,expectedsum):
    if len(remainder)==0:
        if sum(chosen)==expectedsum:
            return chosen
        return False
    return printFirstsum(chosen+[remainder[0]],remainder[1:],expectedsum) or printFirstsum(chosen,remainder[1:],expectedsum)

arr=[1,2,1]
expectedsum=3
# print("printsum",printFirstsum([],arr,expectedsum))

#print count of all the element combination euqal to sum

def printSumCount(chosen,remainder,expectedsum):
    if sum(chosen)>expectedsum:
        return 0
    if len(remainder)==0:
        if sum(chosen)==expectedsum:
            return 1
        return 0
    left=printSumCount(chosen+[remainder[0]],remainder[1:],expectedsum)
    right=printSumCount(chosen,remainder[1:],expectedsum)
    return left+right

arr=[1,2,1]
expectedsum=2

# print("print sum count",printSumCount([],arr,expectedsum))


#print combination sum
ans=[]
# def combinationSum(arr,index,target,ds):
#     if target==0 :
#         ans.append(ds)
#         return
#     if len(arr) == index or target<0:
#         return
#     combinationSum(arr,index,target-arr[index],ds+[arr[index]])
#     combinationSum(arr,index+1,target,ds)

def combinationSum(arr,target,ds):
    if not len(arr) and  target==0 :
        ans.append(ds)
        return
    if not len(arr) or target<0:
        return
    combinationSum(arr,target-arr[0],ds+[arr[0]])
    combinationSum(arr[1:],target,ds)


combinationSum([2,3,6,7],7,[])
print(f"combinationSum {ans}")

ans=[]
def combinationSum2(arr,index,target,ds):
    if target==0 :
        ans.append(ds)
        return
    if len(arr) == index or target<0:
        return
    prevIndex=-1
    for i in range(index,len(arr)):
        if prevIndex==arr[i]:
            continue
        else:
            prevIndex=arr[i]
        if arr[i]>target:
            break

        combinationSum2(arr,i+1,target-arr[i],ds+[arr[i]])

ans=[]
def combinationSum2brute(arr,index,target,ds):
    if target==0 :
        if ds not in ans:
            ans.append(ds)
        return
    if len(arr) == index or target<0:
        return
    combinationSum2brute(arr,index+1,target-arr[index],ds+[arr[index]])
    combinationSum2brute(arr, index + 1, target, ds)
ar=[1,1,1,2,2]
ar.sort()
# print(ar)
combinationSum2brute(ar,0,4,[])
print("combination sum2 bruce ",ans)

ans=[]
def subsetSum(arr,index,res):
    if index==len(arr):
        ans.append(res)
        return
    subsetSum(arr,index+1,res+arr[index])
    subsetSum(arr,index+1,res)
#
# def subsetSum(arr,res):
#     if not len(arr):
#         ans.append(res)
#         return
#     subsetSum(arr[1:],res+arr[0])
#     subsetSum(arr[1:],res)

arr=[3,1,2]
subsetSum(arr,0,0)
# print("subset sum",ans)


#Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
ans=[]
def subset2(arr,index,ds):
    if len(arr)==index:
        if ds not in ans:
            ans.append(ds)
        return
    subset2(arr,index+1,ds+[arr[index]])
    subset2(arr,index+1,ds)

ar=[1,2,2]
subset2(ar,0,[])
print("subset sum2 ",ans)


##print all permutation of  string (using extra map )

ans=[]
def printPermutation(arr,ds,map):
    if len(ds)==len(arr):
        ans.append(ds[:])
        return
    for i in range(0,len(arr)):
        if map[i]==0:
            map[i]=1
            ds.append(arr[i])
            printPermutation(arr,ds,map)
            ds.pop()
            map[i]=0

map=[0]*len(arr)
#
printPermutation([1,2,3],[],map)
print(ans)

#print permutation of string  (without using extra map )
res=[]
def permute(arr,index):
    if index==len(arr):
        res.append(arr[:])
        return
    for i in range(index,len(arr)):
        arr[i],arr[index]=arr[index],arr[i]
        permute(arr,index+1)
        arr[i], arr[index] = arr[index], arr[i]


permute([1,2,3],0)
print("permutation",res)











