import random
def partition(array, l, r):
    x = array[l]
    j = l
    for i in range(l + 1, r + 1):
        if array[i] <= x:
            j += 1
            array[i], array[j] = array[j], array[i]
    array[l], array[j] = array[j], array[l]
    return j
def quicksort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition(a, l, r)
    j = m-1
    while(j>=0 and a[j]==a[m]):
        j-=1
    k = m+1
    while(k<len(a) and a[k]==a[m]):
        k+=1
    quicksort(a, l, j);
    quicksort(a, k, r);
    
n=int(input())
a = list(map(int,input().split()))
quicksort(a, 0, n - 1)
for x in a:
    print(x, end=' ')
