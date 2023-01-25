for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    o = min(a)
    print(o*(n-1))
