def cul(a,z):#找出数组a中比z小的数，这里将l，r化为一个问题
    ans=0
    l,r=1,n
    while l<r:
        if a[l]+a[r]<=z:
            ans+=r-l
            l+=1
        else:
            r-=1
    return ans

n,l,r=map(int,input().split())
a=[0]+list(map(int,input().split()))
a.sort()
print(cul(a,r)-cul(a,l-1))