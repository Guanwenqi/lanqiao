n=int(input())
a=list(map(int,input().split()))
tot=0
for i in range(1<<n):#通过二进制的0和1来区别左走还是右走，恰好枚举所有情况
    ans=0
    for j in range(n):
        if i>>j &1==1:
           ans+=a[j]
        else:
            ans-=a[j]
    if ans%7==0:
        tot+=1
print("{:.4f}".format(tot/(1<<n)+0.000000001))#防止遇到5舍而非进位

# for i in range(1<<3):
    # print(bin(i)[2:].zfill(3))
    # print('{:0>3}'.format(bin(i)[2:]))