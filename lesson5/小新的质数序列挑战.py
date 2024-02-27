from math import *
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if min(a,b)==1:
        print(-1)
    else:
        if gcd(a,b)>1:
            print(0)
        else:
            print(1)