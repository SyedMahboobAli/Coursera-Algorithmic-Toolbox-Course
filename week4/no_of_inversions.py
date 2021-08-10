def count1(arr,temp_arr,left,mid,right):
    i = left
    j = mid+1
    k = left
    count =0 
    while(i<=mid and j<=right):
        if(arr[i]<=arr[j]):
            temp_arr[k] = arr[i]
            k+=1
            i+=1
        else:
            temp_arr[k]  =arr[j]
            count+=(mid-i+1)
            k+=1
            j+=1
    while(i<=mid):
        temp_arr[k]  =arr[i]
        i+=1
        k+=1
    while(j<=right):
        temp_arr[k] = arr[j]
        j+=1
        k+=1
    for x in range(left,right+1):
        arr[x] = temp_arr[x]
    return count

def inversions(arr,b,l, r):
    n = 0
    if(l<r):
        m = l+int((r-l)/2)
        n+=inversions(arr,b,l,m)
        n+=inversions(arr,b,m+1,r)
        n+=count1(arr,b,l,m,r)
    return n
n=int(input())
a = list(map(int, input().split()))
b = [0]*len(a)
ans =inversions(a,b,0, len(a)-1)
print(ans)
