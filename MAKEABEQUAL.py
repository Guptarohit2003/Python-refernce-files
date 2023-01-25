for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    a = 0
    b = 0
    for i in range(n):
        if x[i] > y[i]:
            a += x[i] - y[i]
        elif x[i] < y[i]:
            b += y[i] - x[i]

    if a == b:
        print(a)
    else:
        print(-1)
