import itertools as it
cnt=0
a=0
n=input()
for i in it.permutations('123456789'):
    st=''.join(i)
    for j in range(len(n)):
        a=int(st[:j+1])
        if a>=int(n):
            break
        bl=(int(n)-a)*int(st[-1])%10
        if bl==0:
            continue
        index=st.find(str(bl))
        if index<=j or index>=8:
            continue
        b=int(st[j+1:index+1])
        c=int(st[index+1:])
        if a+b/c==int(n):
            cnt+=1
print(cnt)


