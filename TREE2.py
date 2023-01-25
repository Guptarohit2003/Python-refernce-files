for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    s = set(a)
    if 0 in s:
        s.remove(0)
    print(len(s))

