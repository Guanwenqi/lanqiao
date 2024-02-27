def dfs(depth,s,cnt):
    if s>m:
        return
    if s==m:
        global ans
        ans=min(ans,cnt)
    if depth==n:
        return
    dfs(depth+1,s+a[depth],cnt)
    dfs(depth+1,s+a[depth]//2,cnt+1)
    dfs(depth+1,s,cnt)
n,m=map(int,input().split())
a=list(map(int,input().split()))
m*=2
a=[x*2 for x in a]#对于劈瓜一半的问题，乘2能保证不出现小数存储误差
ans=n+1
dfs(0,0,0)
if ans==n+1:
  ans=-1
print(ans)