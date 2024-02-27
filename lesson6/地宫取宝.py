from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(x,y,z,w):
    if x==n and y==m:
        if z==k:
            return 1
        if z==k-1:
            if w<a[x][y]:
                return 1
        return 0
    ans=0
    for dx,dy in [(1,0),(0,1)]:
        xx,yy=x+dx,y+dy
        if xx<=n and yy<=m:
            ans+=dfs(xx,yy,z,w)
            if w<a[x][y] :
               ans+=dfs(xx,yy,z+1,a[x][y])
    return ans%1000000007
n,m,k=map(int,input().split())
a=[[0]*(m+1)]
for i in range(n):
    a.append([0]+list(map(int,input().split())))
print(dfs(1,1,0,-1))

