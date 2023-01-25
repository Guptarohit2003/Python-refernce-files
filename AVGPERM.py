T=int(input())
for test in range(0,T):
    n=int(input())
    if(n==3):
        print("3 2 1")
    elif(n==4):
        print("4 2 1 3")
    else:
        L=[i for i in range(1,n-3)]
        L=[n,n-2]+L+[n-3,n-1]
        print(*L)