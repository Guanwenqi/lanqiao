mod=998244353
n,x=map(int,input().split())
a=[0]+list(map(int,input().split()))
dp=[[0]*64 for i in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
    for j in range(64):
        dp[i][j]=(dp[i-1][j]+dp[i-1][j^a[i]])%mod
print(dp[n][x])
