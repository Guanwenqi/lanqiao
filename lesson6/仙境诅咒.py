def dis(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2<=d**2
def dfs(x,y):
    for i in range(n):
        if not vis[i] and dis(x,y,w[i][0],w[i][1]):
            vis[i]=True
            dfs(w[i][0],w[i][1])
n=int(input())
w=[list(map(int,input().split())) for i in range(n)]
d=int(input())
vis=[False]*n
vis[0]=True
dfs(w[0][0],w[0][1])
for i in vis:
    print(int(i))

