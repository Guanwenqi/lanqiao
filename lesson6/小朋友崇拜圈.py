import sys
sys.setrecursionlimit(100000)#递归层数过大，要扩栈
def dfs(x,length):
    vis[x]=length
    if vis[a[x]]:
        global ans
        ans=max(ans,length-vis[a[x]]+1)
    else:
        dfs(a[x],length+1)
n=int(input())
a=list(map(int,input().split()))
a=[0]+a
vis=[0]*(n+1)
ans=0
for i in range(1,n+1):
    if vis[i]==0:
        dfs(i,1)
print(ans)



