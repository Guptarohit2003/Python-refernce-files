for _ in range(int(input())):
    C,D,L = map(int,input().split(' '))
    if C > D*2:
        s = C - (D*2)
        mi = D*4 + s*4
    else:
        mi = D*4
    ma = D*4 + C*4
    if L >= mi and L <= ma and L%4 == 0:
        print('yes')
    else:
        print('no')