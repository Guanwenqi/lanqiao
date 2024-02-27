n,k=map(int,input().split())
a=list(map(int,input().split()))
def check(x):
    cnt=0
    for i in range(n):
        cnt+=a[i]//x
    return cnt>=k
ans=0
l,r=1,int(1e9)
while l<=r:
    mid=(l+r)//2
    if check(mid):
        ans=mid
        l=mid+1
    else:
        r=mid-1
if ans==0:
    print(-1)
else:
    print(ans)