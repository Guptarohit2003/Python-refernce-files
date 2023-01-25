for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    maxi=x.index(max(x))
    if maxi==0:
        print(-1)
    else:
        l=x[:maxi]
        r=x[maxi:]
        print(len(l))
        print(*l)
        print(len(r))
        print(*r)