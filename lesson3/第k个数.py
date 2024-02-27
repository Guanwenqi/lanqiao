# 内存占用过大过不了
# n,m=map(int,input().split())
# a=[]
# for i in range(1,n+1):
#    a.append(str(i))
# a.sort()
# print(a)

# 解决方案
def find(n,k):
  cur=1
  k-=1
  while k:
    step=culstep(cur,n)
    if step<=k:
      cur+=1
      k-=step
    else:
      cur*=10
      k-=1
  return cur
def culstep(cur,n):
  step=0
  cur1=cur+1
  while cur<=n:
    step+=min(n+1,cur1)-cur
    cur1*=10
    cur*=10
  return step
n,k=map(int,input().split())
print(find(n,k))