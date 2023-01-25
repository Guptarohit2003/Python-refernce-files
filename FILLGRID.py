for _ in range(int(input())):
    N = int(input())
    if N%2 == 0:
        for i in range(N):
            for j in range(N):
                print('-1',end=' ')
            print(end='\n')
    else:
        for i in range(N):
            for j in range(N):
                if i == j:
                    print('1',end=' ')
                else:
                    print('-1',end= ' ')
            print(end='\n')