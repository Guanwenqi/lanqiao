n=int(input())
a=list(map(int,input().split()))
b=[max(a)]
v=max(a)
a.remove(max(a))
for i in range(30):
    tmp,ind=-1,-1
    for j in range(len(a)):
        if tmp<((v|a[j])-v):#不减去v也对
            tmp=((v|a[j])-v)
            ind=j
    if ind==-1:
        break
    b.append(a[ind])
    v|=a[ind]
    a.remove(a[ind])
print(*b,*a)