def dfs(depth):
    if depth==n:
        print(path)
        return
    for i in range(1,n+1):
        if vis[i] is False:
            vis[i]=True
            path.append(i)
            dfs(depth+1)
            vis[i]=False
            path.pop(-1)
    dfs(n)
n=3
path=[]
vis=[False]*4
dfs(0)