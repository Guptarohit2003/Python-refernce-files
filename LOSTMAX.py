for _ in range(int(input())):
    a = list(map(int,input().split()))
    a.remove(len(a)-1)
    print(max(a))