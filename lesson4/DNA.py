# 通过字典完成碱基配对
# x1={'A':'T','T':'A','C':'G','G':'C'}
# cnt=0
# n=int(input())
# a=list(input())
# b=list(input())
# for i in range(n):
#     if x1[a[i]]!=b[i]:
#         for j in range(i+1,n):
#             if x1[a[i]]==b[j] and x1[a[j]]==b[i]:
#                 a[i],a[j]=a[j],a[i]
#         cnt+=1
# print(cnt)

stone={}
def pre():
  x=1
  cnt=0
  while x<=1e6:
    stone[x]=cnt
    x+=sum(map(int,list(str(x))))
    cnt+=1
pre()
t=int(input())
for i in range(t):
  s=int(input())
  if s in stone.keys():
    print(stone[s])
  else:
    print(-1)
    