def dfs(x):
    ans=0
    if gold[x]==0:
        ans+=w[x]
    if ch[x][0]!=-1:
        l=ch[x][0]-1
        gold[l]=gold[x]+1
        ans+=dfs(l)
    if ch[x][1]!=-1:
        r=ch[x][1]-1
        gold[r]=gold[x]-1
        ans+=dfs(r)
    return ans
n=int(input())
w=list(map(int,input().split()))
ch=[list(map(int,input().split())) for i in range(n)]
gold=[0]*n
print(dfs(0))