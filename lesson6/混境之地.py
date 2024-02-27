from sys import exit
import sys
sys.setrecursionlimit(1000000)
dir=[(0,1),(0,-1),(1,0),(-1,0)]
def dfs(x,y,v):
    vis[x][y]=v
    for i in range(4):
        xx,yy=x+dir[i][0],y+dir[i][1]
        if 0<=xx<n and 0<=yy<m and not vis[xx][yy] and pos[xx][yy]=='.':
            dfs(xx,yy,v)
def check(x,y):
    ans=0
    for i in range(4):
        xx,yy=x+dir[i][0],y+dir[i][1]
        if 0<=xx<n and 0<=yy<m:
            ans|=vis[xx][yy]
    return ans==3#1|2=3,只要满足这个条件，说明两个联通区之间仅有一个墙，打通即可
n,m=map(int,input().split())
a,b,c,d=map(int,input().split())
a,b,c,d=a-1,b-1,c-1,d-1
pos=[list(input()) for i in range(n)]
vis=[[0]*m for i in range(n)]
dfs(a,b,1)
if vis[c][d]==1:
    print("Yes")
else:
    dfs(c,d,2)
    for i in range(n):
        for j in range(m):
            if pos[i][j]=='#' and check(i,j):
               print("Yes")
               exit()
    print("No")