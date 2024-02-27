def dfs(depth):
    if depth==n:
        global ans
        ans+=1
        return
    for i in range(1,n+1):
        if vis1[i] is False and vis2[depth+i] is False and vis3[depth-i+n] is False:
            vis1[i]=True
            vis2[depth+i]=True
            vis3[depth-i+n]=True
            dfs(depth+1)
            vis1[i]=False
            vis2[depth+i]=False
            vis3[depth-i+n]=False
n=int(input())
ans=0
vis1=[False]*(n+1)
vis2=[False]*(2*n+1)
vis3=[False]*(2*n+1)
dfs(0)
print(ans)