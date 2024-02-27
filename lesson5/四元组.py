import math
n=int(input())
li=list(map(int,input().split()))
a=-math.inf
stack=[]
minr=[math.inf]*n
for i in range(n-2,-1,-1):
    minr[i]=min(minr[i+1],li[i+1])
flag=False
for i in range(n):
    if li[i]<a and li[i]>minr[i]:
        print("YES")
        flag=True
        break
    while stack and li[i]>stack[-1]:
        a=max(a,stack[-1])
        stack.pop()
    stack.append(li[i])
if not flag:
    print("NO")


    