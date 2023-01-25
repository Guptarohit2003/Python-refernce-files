for _ in range(int(input())):
    N = int(input())
    S = input()
    a = S.count('0')
    b = N-a
    if a>b:
        print('0'*a)
    else:
        print('1'*b)

    