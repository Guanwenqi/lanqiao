def dfs(depth,lv,tot,mul):
    if depth==n:
        if tot-path[-1]>path[-1]:
            ans[mul]+=1
        return
    for i in range(lv+1,100001):#为了保证多边形不一样，维护单调递增序列
        if mul*(i**(n-depth))>100000:
            break
        path.append(i)
        dfs(depth+1,i,tot+i,mul*i)
        path.pop()
t,n=map(int,input().split())
ans=[0]*100001
path=[]
dfs(0,0,0,1)
for i in range(1,100001):
    ans[i]+=ans[i-1]
for j in range(t):
    l,r=map(int,input().split())
    print(ans[r]-ans[l-1])
