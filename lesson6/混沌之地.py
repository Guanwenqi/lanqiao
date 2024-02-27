from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(x,y,z):
    if x==c-1 and y==d-1:
        return True
    for i in range(4):
        xx,yy=x+dir[i][0],y+dir[i][1]
        if xx<0 or xx>=n or yy<0 or yy>=m:
            continue
        if Map[xx][yy]<Map[x][y]:
            if dfs(xx,yy,z):
               return True
        elif Map[xx][yy]<Map[x][y]+k and z==False:
            if dfs(xx,yy,True):
                return True
    return False
dir=[(1,0),(0,1),(-1,0),(0,-1)]
n,m,k=map(int,input().split())
a,b,c,d=map(int,input().split())
Map=[]
for i in range(n):
    Map.append(list(map(int,input().split())))
if dfs(a-1,b-1,False):
    print("Yes")
else:
    print("No")

