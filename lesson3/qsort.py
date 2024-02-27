def partition(a,left,right):
  index=left+1
  for i in range(left+1,right+1):
    if a[i]<=a[left]:
      a[index],a[i]=a[i],a[index]
      index+=1
  a[left],a[index-1]=a[index-1],a[left]
  return index-1
def qsort(a,left,right):
  if left<right:
    mid=partition(a,left,right)
    qsort(a,left,mid-1)
    qsort(a,mid+1,right)
n=int(input())
a=list(map(int,input().split()))
qsort(a,0,n-1)
print(' '.join(map(str,a)))