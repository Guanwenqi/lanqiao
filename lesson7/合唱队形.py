n=int(input())
a=[0]+list(map(int,input().split()))
dp1=[0]+[1]*n
for i in range(1,n+1):
    for j in range(1,i):
        if a[j]<a[i]:
            dp1[i]=max(dp1[i],dp1[j]+1)
dp2=[0]+[1]*n
for i in range(n,0,-1):
    for j in range(i+1,n+1):
        if a[i]>a[j]:
            dp2[i]=max(dp2[i],dp2[j]+1)
ans=max(dp1[i]+dp2[i]-1 for i in range(1,n+1))
print(n-ans) 