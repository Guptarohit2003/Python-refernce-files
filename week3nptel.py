def contracting(l):
    flag = False
    for i in range(1,len(l)-1):
        if abs(l[i-1]-l[i]) > abs(l[i]-l[i+1]):
            flag = True
        else:
            flag = False
            break
    if flag == True:
        return True
    else:
        return False


def counthv(l):
    hc = 0
    vc = 0
    for i in range(1,len(l)-1):
        if l[i] > l[i-1] and l[i] > l[i+1]:
            hc +=1
        elif l[i] < l[i-1] and l[i] < l[i+1]:
            vc += 1
    x = [hc,vc]
    return x

def leftrotate(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[j][N-1-i]
            A[j][N-1-i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = temp
    return A
