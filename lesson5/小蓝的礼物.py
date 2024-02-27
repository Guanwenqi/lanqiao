from itertools import accumulate
import math
n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=0
a.sort()
for i in range(n):
    if k>=a[i]:
        ans+=1
        k-=a[i]
    else:
        if k>=math.ceil(a[i]/2):
            ans+=1
        break
print(ans)