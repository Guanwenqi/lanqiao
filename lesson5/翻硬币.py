ini=list(input())
cor=list(input())
n=len(ini)
ans=0
for i in range(n-1):
    if ini[i]==cor[i]:
        continue
    if ini[i]!=cor[i]:
        if ini[i+1]=='*':
            ini[i+1]='o'
            ans+=1
        else:
            ini[i+1]='*'
            ans+=1
print(ans)