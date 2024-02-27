import sys
sys.setrecursionlimit(100000000)
dir=[(1,0),(0,1),(-1,0),(0,-1)]
def dfs(x,y):
    vis[x][y]=1
    if map[x][y+1]=='#' and map[x][y-1]=='#' and map[x+1][y]=='#' and map[x-1][y]=='#':
        global flag
        flag=1
    for i in range(4):
        xx,yy=x+dir[i][0],y+dir[i][1]
        if map[xx][yy]=='#' and vis[xx][yy]==0:
            dfs(xx,yy)
n=int(input())
map=[]
vis=[]
for i in range(n):
    map.append(list(input()))
    vis.append([0]*n)
ans=0
for i in range(n):
    for j in range(n):
        if map[i][j]=='#'and vis[i][j]==0:
            flag=0
            dfs(i,j)
            if flag==0:
                ans+=1
print(ans)
'''
7
.......
.##....
.##....
....##.
..####.
...###.
.......
'''
