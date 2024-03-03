n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
dp=[[0]*n for i in range(n)]
for i in range(n-1,-1,-1):
    for j in range(i+1):
        if i==n-1:
            dp[i][j]=a[i][j]
        else:
            dp[i][j]=max(dp[i+1][j],dp[i+1][j+1])+a[i][j]
print(dp[0][0])