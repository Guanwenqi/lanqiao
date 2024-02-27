w=int(input())
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
a.sort()
ans=0
l,r=0,n-1
while True:
    if l==r:
        ans+=1
        break
    elif l>r:
        break
    if a[l]+a[r]<=w:
        l+=1
        r-=1
        ans+=1
    else:
        r-=1
        ans+=1
print(ans)