n,k=map(int,input().split())
z=list(map(int,input().split()))
b=list(map(int,input().split()))
cha=[b[i]-z[i] for i in range(n)]
cha.sort(reverse=True)
ans=sum(z)
for i in range(k):
    if cha[i]<0:
        break
    ans+=cha[i]
print(ans)
