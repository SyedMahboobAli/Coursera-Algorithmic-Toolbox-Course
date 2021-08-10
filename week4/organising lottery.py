#Uses python3
import sys

def binarysearch(ranges,value,l,r):
    ans = r
    while(l<=r):
        m = l+int((r-l)/2)
        if(ranges[m][0]>=value):
            ans = m
            r = m-1
        else:
            l = m+1
    return ans

def fast_count_segments(starts, ends, points):
    ranges = []
    n = len(starts)
    for i in range(n):
        ranges.append([starts[i],ends[i]])
    ranges.sort(key=lambda x:x[0])
    cnt = []
    for i in points:
        pos = binarysearch(ranges,i,0,n-1)
        count = 0
        while(pos>=0):
            if(ranges[pos][0]<=i and ranges[pos][1]>=i):
                count+=1
            pos-=1
        cnt.append(count)
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
