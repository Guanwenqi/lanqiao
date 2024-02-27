import sys
input=sys.stdin.readline#加快输入输出速度
itc='0123456789ABCDEF'
cti={}
for index,char in enumerate(itc):
  cti[char]=index
def mtoten(m,a):
  ans=0
  for char in a:
    ans=ans*m+cti[char]
  return ans
# def tenton(ans,n):
#   if ans==0:
#     return
#   tenton(ans//n,n)
#   print(itc[ans%n],end='')
def Tenton(ans,n):
  Ans=''
  while ans!=0:
    Ans+=itc[ans%n]
    ans//=n
  return Ans[::-1]#字符串翻转(step为负数时，默认start初始值为-1，stop相应为负数)
t=int(input().strip())
for i in range(t):
  m,n=map(int,input().strip().split())#删除可能输入的多余空格

  a=input().strip()
  A=mtoten(m,a)
  print(Tenton(A,n))
#   tenton(A,n)
#   print()
# 当前方法效率更高