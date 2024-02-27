from bisect import *
n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
pre=[0]*n
for i in range(n):
    pre[i]=(n-1-i)*(n-2-i)//2#运用组合知识
    if i>0:
        pre[i]+=pre[i-1]#节省大量空间
for i in range(q):
    qq=int(input())
    ind=bisect_left(pre,qq)
    print(a[ind])
