import math
n,x=map(int,input().split())
s=list(input())
s.sort()
if s[0]==s[x-1]:
  if s[x]==s[-1]:
    print(''.join([s[0]]+[s[x]]*math.ceil((n-x)/x)))
  else:
    print(''.join([s[0]]+s[x:]))
else:
  print(''.join(s[x-1:]))