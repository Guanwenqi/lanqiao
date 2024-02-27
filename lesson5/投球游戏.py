from itertools import accumulate
n,q=map(int,input().split())
a=list(map(int,input().split()))
diff=[0]*(n+1)
diff[0]=a[0]
for i in range(1,n):
  diff[i]=a[i]-a[i-1]
for i in range(q):
  l,r,c=map(int,input().split())
  diff[l-1]+=c
  diff[r]-=c
li=list(accumulate(diff))
print(*li[:-1])