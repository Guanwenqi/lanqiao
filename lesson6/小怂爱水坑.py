import sys
sys.setrecursionlimit(1000000)
dir=[(1,0),(-1,0),(0,1),(0,-1)]
def dfs(x,y):
    vis[x][y]=True
    ans=w[x][y]
    for i in range(4):
        xx,yy=x+dir[i][0],y+dir[i][1]
        if 0<=xx<n and 0<=yy<m and not vis[xx][yy] and w[xx][yy]!=0:
            ans+=dfs(xx,yy)
    return ans

n,m=map(int,input().split())
w=[list(map(int,input().split()))for i in range(n)]
vis=[[False]*m for i in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        if not vis[i][j] and w[i][j]!=0: 
            ans=max(ans,dfs(i,j))
print(ans)
# 以下两种表达式不一样，第一个是分别定义n个列表；第二个是指引用同一个列表n次，修改那个列表一次，其他都会变，导致答案错误
# vis=[[False]*m for i in range(n)]
# vis=[[False]*m]*n


