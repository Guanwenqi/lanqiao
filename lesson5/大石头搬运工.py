import math
n=int(input())
li=[]
for i in range(n):
    li.append(list(map(int,input().split())))
li.sort(key=lambda x:x[1])
pre=[0]
nex=[0]
s1=li[0][0]
s2=li[-1][0]
for i in range(1,n):
    pre.append(pre[-1]+(s1)*(li[i][1]-li[i-1][1]))
    s1+=li[i][0]
for i in range(n-2,-1,-1):
    nex.append(nex[-1]+(s2)*(li[i+1][1]-li[i][1]))
    s2+=li[i][0]
nex.reverse()
res=math.inf
# print(type(res))
for i in range(n):
    res=min(res,pre[i]+nex[i])
print(res)
