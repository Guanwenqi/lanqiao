# n,m,k=map(int,input().split())
# tot=10*24*60*60
# a=[[0 for i in range(tot+1)]for j in range(n+1)]
# for i in range(m):
#     d,h,m,s,x=map(int,input().split())
#     time=(d-1)*24*60*60+h*3600+m*60+s
#     a[x][time]+=1
#     cnt=sum(a[x][max(0,time-60+1):time+1])
#     if cnt>=k:
#       for j in range(max(0,time-60+1),time+1):
#         a[x][j]=0
# for i in range(1,n+1):
#     print(sum(a[i]))

from itertools import product
a=list(product([1,2,3],repeat=2))
print(a,type(a))