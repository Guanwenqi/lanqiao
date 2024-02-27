m,n=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
country=[]
flag=True
for i in range(n):
    tmp=list(map(int,input().split()))
    k=tmp[0]
    tmp=tmp[1:]
    if k>m:
        flag=False
        break
    tmp.sort()
    tmp=[0]*(m-k)+tmp
    country.append(tmp)
if flag:
    ma=[]
    for j in range(m):
        ma.append(0)
        for i in range(n):
            ma[j]=max(ma[j],country[i][j])
    round=0
    peo=0#双指针
    while round<m and ma[round]==0:
        round+=1
    ans=0
    while round<m and peo<m:
        if ma[round]<=a[peo]:
            ans+=a[peo]
            round+=1
        peo+=1
    if round==m:
        print(ans)
    else:
        print(-1)
else:
    print(-1)



