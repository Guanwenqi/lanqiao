from bisect import *
n=int(input())
a=list(map(int,input().split()))
a.sort()
ind=bisect_left(a,0)
tot=sum(a[ind:])
if(n-ind)%2!=0:
    if ind:
        tot-=min(abs(a[ind-1]),a[ind])
    else:
        tot-=a[0]
print(tot)
