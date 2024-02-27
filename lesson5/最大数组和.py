import math
from itertools import accumulate
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    li.sort()
    pre=[0]+list(accumulate(li))
    ans=-math.inf
    for i in range(k+1):
        ans=max(ans,pre[n-(k-i)]-pre[2*i])
    print(ans)

