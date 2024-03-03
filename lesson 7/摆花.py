n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
dp=[[0] *(m+1) for i in range(n+1)]
for i in range(n+1):
    dp[i][0]=1
for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(min(a[i],j)+1):
            dp[i][j]+=dp[i-1][j-k]
            dp[i][j]%=1000007
print(dp[n][m])