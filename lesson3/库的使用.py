# from itertools import combinations
# from heapq import nlargest
# n=int(input())
# a=list(map(int,input().split()))
# res=set()#自动去重功能
# for i in combinations(a,3):
#     res.add(sum(i))
# res=list(res)
# # res.sort()
# # print(res[-3])
# print(nlargest(3,res)[-1])

t=int(input())
for m in range(t):
  n,k=map(int,input().split())
  a=list(map(int,input().split()))
  ans=n
  for i in range(1,61):
    j=0
    cnt=0
    while j<n:
      if a[j]!=i:
        j+=k
        cnt+=1  
      else:
        j+=1
    ans=min(ans,cnt)
  print(ans)
