for _ in range(int(input())):
    N,K = map(int,input().split())
    S = str(input())
    l = [i for i in S]
    flag = 1
    v = 0
    for i in range(N//2):
        if l[i] != l[-i-1]:
                v +=1
    if K >= v:
        if N%2 != 0:
            print("YES")
        else:
            if (K-v)%2 == 0:
                print("YES")
            else:
                print("NO")
    else:
        print("NO")
