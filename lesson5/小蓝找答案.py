def add(stk,pos,k):
  while len(stk)>1 and stk[-1][0] >pos:
    stk.pop()
  if stk[-1][0]==pos:
    stk[-1][1]+=1
  else:
    stk.append([pos,1])
  if len(stk) >1 and stk[-1][1]==k:
    add(stk,pos-1,k)

def check(k):
  stk=[[0,0]]
  for i in range(1,n):
    if s[i-1]>=s[i]:
      if k==1:
        return False
      add(stk,s[i],k)
    if stk[0][1]:
      return False
  return True

def find(l,r):
  while l+1<r:
    mid=-(-(l+r)//2)
    if check(mid):
      r=mid
    else:
      l=mid
  return r

n=int(input())
s=list(map(int,input().split()))
print(find(1,n))