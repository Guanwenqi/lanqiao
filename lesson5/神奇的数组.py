n=int(input())
a=list(map(int,input().split()))
yh=[0]
add=[0]
for i in range(n):
    add.append(add[-1]+a[i])
    yh.append(yh[-1]^a[i])
l,r=1,1
ans=0
while l<=n and r<=n:
    while l<=n and r<=n and (add[r]-add[l-1])==(yh[r]^yh[l-1]):#仿照前缀和的思路
        ans+=(r-l+1)#恰好解决组合问题
        r+=1
    l+=1
print(ans)

