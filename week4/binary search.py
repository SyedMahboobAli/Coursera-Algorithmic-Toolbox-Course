def binarysearch(l1,low,high,k ):
    while(low<=high):
        mid=low+(high-low)//2
        if(l1[mid]==k):
            return mid
        elif(l1[mid]>k):
            return binarysearch(l1,low,mid-1,k)
        elif(l1[mid]<k):
            return binarysearch(l1,mid+1,high,k)
    else:
        return -1
    
a=list(map(int,input().split()))
n=a[0]
l1=a[1:]
a=list(map(int,input().split()))
m=a[0]
l2=a[1:]
for i in range(len(l2)):
    x=binarysearch(l1,0,len(l1)-1,l2[i])
    print(x,end=' ')
