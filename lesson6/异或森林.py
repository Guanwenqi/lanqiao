n=int(input())
a=list(map(int,input().split()))
pre=[0]*n
pre[0]=a[0]
for i in range(1,n):
    pre[i]=pre[i-1]^a[i]
ans=0
for x in range(0,200):
    xor=x*x
    dic={}
    dic[0]=1#由于l==0时，l-1本身并不存在，所以假定pre数组起始位置前有一个0
    for j in range(n):
        ans+=dic.get(pre[j]^xor,0)
        dic[pre[j]]=dic.get(pre[j],0)+1
ans=n*(n+1)//2-ans#由于加入附加的0，数组长度视为（N+1）
print(ans)

