l,n,m=map(int,input().split())
d=[]
for i in range(n):
    d.append(int(input()))
def check(x):
    ni=0
    cnt=0
    for i in range(n):
        if d[i]-ni<x:
            cnt+=1
        else:
            ni=d[i]
    if l-ni<x:
        return False
    return cnt<=m
left,right,ans=1,l,1
while left<=right:
    mid=(left+right)//2
    if check(mid):
        ans=mid
        left=mid+1
    else:
        right=mid-1
print(ans)
