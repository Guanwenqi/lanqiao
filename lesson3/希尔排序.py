# n=int(input())
# a=list(map(int,input().split()))
# gap=n//2
# while gap:
#     for i in range(gap,n):
#         value=a[i]
#         j=i
#         while j>=gap:
#             if a[j-gap]>value:
#                 a[j]=a[j-gap]
#                 j-=gap
#             else:
#                 break
#         a[j]=value
#     gap//=2
# print(*a)
# def cmp(value,j):
#   if a[j-gap][1]>value[1]:
#     return True
#   elif a[j-gap][1]==value[1] and a[j-gap][0]>value[0]:
#     return True
#   else:
#     return False
# n=int(input())
# a=[]
# for i in range(n):
#   a.append(list(map(int,input().split())))
# gap=n//2
# while gap:
#     for i in range(gap,n):
#         value=a[i]
#         j=i
#         while j>=gap:
#             if cmp(value,j):
#                 a[j]=a[j-gap]
#                 j-=gap
#             else:
#                 break
#         a[j]=value
#     gap//=2
# for i in a:
#    print(i[0])

n=int(input())
m=int(input())
gap=list(map(int,input().split()))
a=[]
for i in range(n):
  a.append(int(input()))
compare=0
change=0
for t in gap:
    for i in range(t,n):
        value=a[i]
        j=i
        while j>=t:
            if a[j-t]>value:
                a[j]=a[j-t]
                j-=t
                compare+=1
                change+=1
            else:
                compare+=1
                break
        a[j]=value
print(compare,change)

