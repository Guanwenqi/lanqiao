from bisect import *
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
aa=[0]
bb=[0]
for i in range(n):
    aa.append(aa[-1]+a[i])
for i in range(m):
    bb.append(bb[-1]+b[i])
ans=0
for i in range(n+1):
    if aa[i]>k:
        break
    res=k-aa[i]
    ind=bisect_right(bb,res)
    ans=max(ans,ind+i-1)
print(ans)
