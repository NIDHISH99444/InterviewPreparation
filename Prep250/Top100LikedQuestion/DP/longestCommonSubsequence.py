def lcs(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    t=[[0 for i in range(m+1) ]for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if arr1[i-1]==arr2[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    for ele in t:
        print(ele)
    return t[-1][-1]






text1 = "abcde"
text2 = "abce"
print(lcs(text1,text2))