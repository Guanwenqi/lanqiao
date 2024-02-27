from itertools import accumulate
def getpresum(a):
  suml=list(accumulate(a))
  return suml
def getsum(suml,l,r):
  if l==0:
    return suml[0]
  else:
    return suml[r]-suml[l-1]
s=input()
n=len(s)
a=[]
for x in s:
  if x=='L':
    a.append(1)
  else:
    a.append(-1)
suml=getpresum(a)
ans=0
for i in range(n):
  for j in range(i,n):
    if getsum(suml,i,j)==0:
      ans=max(ans,j-i+1)
print(ans)