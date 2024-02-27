n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
odd,even=0,0
for i in range(n):
    if a[i]%2==0:
        even+=1
    else:
        odd+=1
    if even==odd and i!=n-1:
        b.append(abs(a[i]-a[i+1]))
b.sort()
res,flag=0,0
L=len(b)
if m<b[0]:
    print(0)
else:
    for i in range(L):
        res+=b[i]
        if res>m:
            print(i)
            flag=1
            break
    if flag==0:
        print(L)
    


