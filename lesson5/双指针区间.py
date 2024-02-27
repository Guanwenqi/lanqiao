# n,s=map(int,input().split())
# a=list(map(int,input().split()))
# l,r=0,0
# t=0
# len=n+1
# while l<n:
#     while r<n and t<s:
#         t+=a[r]
#         r+=1
#     if t>=s:
#         len=min(len,r-l)
#     t-=a[l]
#     l+=1
# if len<=n:
#     print(len)
# else:
#     print(0)
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
t=0
ans=0
l,r=0,0
while l<n:
  while r<n and t<k:
    if a[r]>=m:
      t+=1
    r+=1
  if t>=k:
    ans+=n-r+1
  if a[l]>=m:
    l+=1
    t-=1
  else:
    l+=1
print(ans)