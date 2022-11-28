


def houseRobbery(arr,index,dp):
    if index==0:
        return arr[index]
    if index==-1:
        return 0
    if dp[index]!=-1:
        return  dp[index]
    pick = arr[index]+houseRobbery(arr,index-2,dp)
    notpick = houseRobbery(arr,index-1,dp)
    dp[index]=max(pick,notpick)
    return dp[index]

arr = [2,7,9,3,1]

n=len(arr)-1
dp=[-1]*(len(arr))
print(houseRobbery(arr,n,dp))
print(dp)