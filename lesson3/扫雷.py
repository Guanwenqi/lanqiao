# row,col=map(int,input().split())
# a=[]
# for i in range(row):
#     a.append(list(map(int,input().split())))
# b=[[0]*col for i in range(row)]
# # 方向数组(八个方向)
# dir=[(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
# for i in range(row):
#     for j in range(col):
#         if a[i][j]==1:
#             b[i][j]=9
#         else:
#             for k in range(8):
#                 x,y=i+dir[k][0],j+dir[k][1]
#                 if 0<=x<row and 0<=y<row:
#                     b[i][j]+=a[x][y]
#         print(b[i][j],end=' ')
#     print()

row,col=map(int,input().split())
Map=[]
ans=[[0]*col for i in range(row)]
for i in range(row):
  a=list(map(int,input().split()))
  Map.append(a)
for i in range(row):
  for j in range(col):
    tot=0
    cnt=0
    for dx in range(-1,2):
      for dy in range(-1,2):
        x,y=i+dx,j+dy
        if 0<=x<row and 0<=y<col:
          tot+=Map[i][j]
          cnt+=1
    ans[i][j]=int(tot/cnt)
    print(ans[i][j],end=' ')
  print()