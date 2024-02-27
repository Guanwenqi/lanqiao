a=list(input())
n=len(a)
l,r=0,n-1
flag=1
while True:
    if l>=r:
        break
    if a[l]!=a[r]:
        flag=0
        break
    else:
        l+=1
        r-=1
if flag:
    print('Y')
else:
    print("N")