for _ in range(int(input())):
    n,m=   map(int,input().split())
    a = list(map(int,input().split()))
    if len(a) == 1:
        print("YES")
    if a[0] > m:
        st = 1
        ed = a[0]
    if a[0] < m:
        st = a[0]
        ed = max(a)
    else:
        z = 0
        for i in range(1,n):
            if a[i] in range(st,ed):
                if a[i] > m:
                    ed = a[i]
                if a[i] < m:
                    st = a[i]
            else:
                z =1
                print("NO")
                break
        if z == 0:
            print("YES")


