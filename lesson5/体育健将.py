from bisect import *
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
li=[[a[i]+b[i],a[i],b[i]] for i in range(n)]
li.sort(key=lambda x:x[0])
pre=[li[0][0]]
for i in range(1,n):
    pre.append(pre[-1]+li[i][0])
ans=0
for i in range(n):
    if k<li[i][1]:
        continue
    tmp=k-li[i][1]
    num=bisect_right(pre,tmp)
    if num<=i:
        ans=max(ans,num+1)
    elif num>=n:
        ans=max(ans,n)
    else:#以第i个为最后情况下的金牌总数
        ans=max(ans,bisect_right(pre,k+li[i][2]))
print(ans)