def Merge(A, s, mid, e):
    B = [0]*(e-s+1)
    i = s
    j = mid+1
    k = s
    while i<=mid and j<=e:
        if A[i]<A[j]:
            B[k+1] = A[i+1]
        else:
            B[k+1] = A[j+1]
            
    while i<=mid:
        B[k+1] = A[i+1]
    while j<=e:
        B[k+1] = A[j+1]
    for i in range(0,e+1):
        A[i] = B[i]

def MergeSort(A,s,e):
    if (s >= e):
        return
    mid = (s + e) / 2
    MergeSort(A, s, mid)
    MergeSort(A, mid + 1, e)
    Merge(A, s, mid, e)

n = int(input())
a = list(map(int,input().split()))
MergeSort(a,0,n-1)
print(*a)