# from functools import lru_cache
# @lru_cache(maxsize=None)若这里不用记忆化搜索的库，可以自己手搓四维数组记录结果
def dfs(x,y,v,depth):
    if depth>k:
        return 0
    if x>=n or y>=m:
        return 0
    if path[x][y]=='#':
        return 0
    if x==(n-1) and y==(m-1):
        return 1
    if f[x][y][v][depth]!=-1:
        return f[x][y][v][depth]
    ans=0
    for i in range(2):
        xx,yy=x+dir[i][0],y+dir[i][1]
        ans+=dfs(xx,yy,i,depth+(i!=v))
    f[x][y][v][depth]=ans
    return ans
dir=[(0,1),(1,0)]  
a=0
n,m,k=map(int,input().split())
path=[input() for i in range(n)]
f=[[[[-1]*6 for i in range(3)]for i in range(m+1)]for i in range(n+1)]#不好直接想象，可以按照维度顺序的逆序依次书写变量，类比二维数组定义方法
if path[0][1]=='.':
    a+=dfs(0,1,0,0)
if path[1][0]=='.':
    a+=dfs(1,0,1,0)
print(a)


