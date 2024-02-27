n,k=map(int,input().split())
a=list(map(int,input().split()))
def check(x):
    res=0
    for i in range(n):
        res+=min(a[i],x)
    return res>=x*k#这个判断要学会，可以先从必要性角度考虑
l,r=0,2*10**14
ans=0
while l<=r:
    mid=(l+r)//2
    if check(mid):
        ans=mid
        l=mid+1
    else:
        r=mid-1
print(ans)
