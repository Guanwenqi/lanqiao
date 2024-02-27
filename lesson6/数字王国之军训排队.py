def check(x,g):
    for y in g:
        if x%y==0 or y%x==0:
            return False
    return True
def dfs(depth):
    global ans
    if len(group)>=ans:
        return
    if depth==n:
        ans=min(ans,len(group))
        return
    for i in group:
        if check(a[depth],i):
            i.append(a[depth])
            dfs(depth+1)
            i.pop()
    group.append([a[depth]])
    dfs(depth+1)
    group.pop()
n=int(input())
a=list(map(int,input().split()))
ans=n
group=[]
dfs(0)
print(ans)