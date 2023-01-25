for _ in range(int(input())):
    a,b,A,B,A1,B1 = map(int,input().split())
    if (a == A and b == B) or (a == B and b == A):
        print(1)
    elif (a == A1 and b == B1) or (a == B1 and b == A1):
        print(2)
    else:
        print(0)