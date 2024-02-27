# n=int(input())
# for i in range(1,n+1,2):
#     print(i,end=' ')
# a=int(input())
# a=not(a)
# print(a,type(a))
# n=int(input())
# cnt=0
# for i in range(1,n+1):
#    i=str(i)
#    if '2' not in i:
#      cnt+=1
# print(cnt)
# N=4
# for i in range(1,N+1):
#     print(' '*(N-i)+'*'*((i*2)-1))
# for i in range(N-1,0,-1):
#     print(' '*(N-i)+'*'*((i*2)-1))
N=4
for i in range(1,N+1):
    print(('*'*(i*2-1)).center(N*2-1))
for i in range(N,0,-1):
    print(('*'*(i*2-1)).center(N*2-1))

