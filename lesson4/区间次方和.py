from itertools import accumulate
MOD=1e9+7
def getpresum(a):
  sum=list(accumulate(a))
  sum=[x%MOD for x in sum]
  return sum
def getsum(sum,l,r):
  if l==0:
    return sum[r]
  else:
    return (sum[r]-sum[l-1]+MOD)%MOD
n,m=map(int,input().split())
a=list(map(int,input().split()))
sumlist=[]
for i in range(1,6):
  sumlist.append(getpresum([x**i for x in a]))#由于时间限制，不能对每次输入的序列进行乘方运算
for i in range(m):
  l,r,k=map(int,input().split())
  print(getsum(sumlist[k-1],l-1,r-1))

  