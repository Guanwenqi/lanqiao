mod=int(1e9+7)
N=100010
n,m=map(int,input().split())
vis=[0]*N
f=[0]*N
a=list(map(int,input().split()))
for x in a:
    vis[x]=1
f[0]=1
f[1]=1-vis[1]
for i in range(2,n+1):
    if vis[i]:
        continue
    f[i]=(f[i-1]+f[i-2])%mod
print(f[n])