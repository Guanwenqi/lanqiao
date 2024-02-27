from itertools import accumulate
import sys
input=sys.stdin.readline
output=sys.stdout.write
n,q=map(int,input().split())
a=list(map(int,input().split()))
a_bit=[]
for i in range(31):
    nb=[]
    for x in a:
        nb.append((x>>i)&1)
    a_bit.append(list(accumulate(nb)))
for i in range(q):
    l,r=map(int,input().split())
    l,r=l-1,r-1
    ans=0
    for j in range(31):
        if l==0:
            now=a_bit[j][r]
        else:
            now=a_bit[j][r]-a_bit[j][l-1]
        if now>0:
            ans+=(1<<j)
    print(str(ans)+'\n')#配合快速输出