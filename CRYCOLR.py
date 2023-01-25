for _ in range(int(input())):
    N = int(input())
    R1,G1,B1 = map(int,input().split())
    R2,G2,B2 = map(int,input().split())
    R3,G3,B3 = map(int,input().split())
    print(max(G1+B1+B2,R2+R3+G3))
