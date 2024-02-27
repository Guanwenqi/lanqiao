# n=int(input())
# a=list(map(int,input().split()))
# maxl=len(str(max(a)))
# for i in range(n):
#   a[i]=str(a[i])
#   while len(a[i])<maxl:
#     a[i]='0'+a[i]
# # print(a[1][-2])
# for j in range(maxl-1,-1,-1):
#   a.sort(key=lambda x:x[j])
# print(*list(map(int,a)))

from math import gcd
# def gcd(a,b):
#   if a%b==0:
#     return b
  # return math.gcd(b,a%b)
def lcm(a,b):
  return a*b/gcd(a,b)
n=int(input())
a,b,c=map(int,input().split())
print(int(n-(n//a+n//b+n//c-n//lcm(a,b)-n//lcm(a,c)-n//lcm(b,c)+n//lcm(a,int(lcm(b,c))))))