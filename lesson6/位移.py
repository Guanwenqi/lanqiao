import sys
# 法一
# input=sys.stdin.readline
# t=int(input())
# for i in range(t):
#     a,b=map(int,input().split())
#     binb=bin(b)[2:].strip('0')
#     bina=bin(a)[2:]
#     if binb in bina:
#         print("Yes")
#     else:
#         print("No")
# 法二
def get(a):
    e,s=31,0
    while(s<=e and (a>>e)&1==0):e-=1
    while (s<=e and (a>>s)&1==0):s+=1
    ans=''
    for i in range(e,s-1,-1):
        ans+=str((a>>i)&1)
    return ans
t=int(input())
for i in range(t):
    a,b=map(int,sys.stdin.readline().strip('\n').split())
    binb=get(b)
    bina=get(a)
    if binb in bina:
        print("Yes")
    else:
        print("No")

    