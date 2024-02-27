from itertools import accumulate
n,w=map(int,input().split())
N=200010
diff=[0]*N
for i in range(n):
    s,t,p=map(int,input().split())
    diff[s]+=p
    diff[t]-=p
a=list(accumulate(diff))
if w>=max(a):
    print("Yes")
else:
    print("No")
