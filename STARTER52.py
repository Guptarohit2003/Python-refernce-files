# def gcd(a,b):
#     if b>a:
#         return gcd(b,a)
#     elif b==0:
#         return a
#     else:
#         return gcd(b,a%b)

# for _ in range(int(input())):
#     N = int(input())
#     A = list(map(int,input().split()))
#     for i in range(N):
#         for j in range(i+1,N):
#             if A[i] > A[j]:
#                 A[i] = gcd(A[i],A[j])
#             else:
#                 A[j] = gcd(A[i],A[j])
#     print(sum(A))


'''from math import gcd


def solve():
    N = int(input())
    A = list(map(int,input().split()))
    min_gcd = 1000000000000
    for i in range(N-1):
        x = gcd(A[i],A[i+1])
        if x<min_gcd:
            min_gcd = x
    return min_gcd*N
for _ in range(int(input())):
    print(solve())'''

'''for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a >b or c >b:
        print("No")
    else:
        print("Yes")'''

# for _ in range(int(input())):
#     n = int(input())
#     s = list(map(int,input().split()))
#     v = [*input()]
#     print(v)

#starters 55
# def func(a,x):
#     for i in a:
#         if i == x:
#             a.remove(i)
#     return

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# for i in range(len(b)):
#     func(a,b[i])
# print(a)

