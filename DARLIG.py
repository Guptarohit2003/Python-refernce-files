for _ in range(int(input())):
    N,K = map(int,input().split())
    if K == 0 and N %4 == 0:
        print("off")
    elif K == 1 and N%4 == 0:
        print("On")
    else:
        if K == 0:
            print("On")
        if K == 1:
            print("Ambiguous")

    