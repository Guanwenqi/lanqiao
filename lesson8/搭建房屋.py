mod=int(1e9)+7
n,m,k=map(int,input().split())
f=[[0]*(k+1) for i in range(n+1)]
for i in range(k+1):
    f[0][i]=1
for i in range(1,n+1):
    for j in range(k+1):
        for z in range(1,m+1):
            if j>=z:
                f[i][j]=(f[i][j]+f[i-1][j-z])%mod
print(f[n][k])
