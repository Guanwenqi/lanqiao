mod=int(1e9+7)
n,k=map(int,input().split())
dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    if i-k-1>=0:
        dp[i]=(dp[i-1]+dp[i-k-1])%mod
    else:
        # 不放置，则dp【i-1】后添0；放置，则只有1种情况，此处填1，前面都为0
        dp[i]=(dp[i-1]+1)%mod
print(dp[n])