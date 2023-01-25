# for _ in range(int(input())):
#     X = int(input())
#     X = X*60
#     Y = X//30
#     print(Y)



# for _ in range(int(input())):
#     X = int(input())
#     if X <= 100:
#         print(X)
#     elif X in range(100,1001):
#         print(X-25)
#     elif X in range(1001,5001):
#         print(X-100)
#     else:
#         print(X-500)



# for _ in range(int(input())):
#     A,B = map(int,input().split())
#     a = min(A,B)
#     b = max(A,B)
#     for i in range(10):
#         if b == a:
#             print("YES")
#             break
#         elif a < b:
#             while a<b:
#                 a = a*2
#         else:
#             print("NO")
#             break



# for _ in range(int(input())):
#     x = int(input())
#     p = list(map(int,input().split()))
#     sum = 0
#     b = []
#     if x == 2:
#         print(p[0]*2)
#     else:
#         for i in range(len(p)):
#             sum += p[i]
#             b.append(p[i])
#             p[i] = sum
#         for j in range(len(p)-1):
#             diff = p[j+1] - b[j]
#             if diff>0:
#                 b[j+1] = b[j] + diff + b[j+1]
#             else:
#                 b[j+1] = b[j] + b[j+1]
#         print(b[i])

# for _ in range(int(input())):
#     n = int(input())
#     x = list(map(int,input().split()))
#     s = 0
#     m = 0
#     for i in range(len(x)):
#         s += x[i]
#         m = max(x[i],m)
#     print(s+m)




# def func():
#     x = int(input())
#     for i in range(1,int(x**0.5)):
#         if (x - 2*i)%(2+i) == 0 and x != 2*i:
#             return "YES"
#     return "NO"


# for _ in range(int(input())):
#     print(func())

'''for _ in range(int(input())):
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    b = a.copy()
    for i in range(y):
        b.sort()
        z = (x^b[0])
        b[0] = z
        if i >1 and b[0] == a[0]:
            break
    b.sort()
    print(*b)'''


from heapq import heappop,heappush

for _ in range(int(input())):
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))

    min_heap = []
    for i in a:
        heappush(min_heap,(i,False))
    
    for j in range(y):
        u = heappop(min_heap)

        if u[1]:
            z = y - j
            if z%2 == 0:
                heappush(min_heap, u)
            else:
                heappush(min_heap,(u[0]^x,True))
            break
        heappush(min_heap,(u[0]^x,True))
    res = ""
    while min_heap:
        res += str(heappop(min_heap)[0]) + " "
    
    print(res)