for _ in range(int(input())):
    N,X =  map(int,input().split())
    A = list(map(int,input().split()))
    if sum(A) < X:
        print("-1")
    elif max(A) >= X:
        print('1')
    else:
        A.sort(reverse=True)
        count = 0
        sum1 = 0
        for i in range(len(A)):
            if sum1<X:
                sum1+=A[i]
                count +=1
        print(count)

            