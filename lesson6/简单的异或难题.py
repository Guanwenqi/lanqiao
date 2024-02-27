n,m=map(int,input().split())
a=list(map(int,input().split()))
pre=[0]
for i in range(n):
    pre.append(pre[-1]^a[i])
for i in range(m):
    l,r=map(int,input().split())
    print(pre[r]^pre[l-1])
