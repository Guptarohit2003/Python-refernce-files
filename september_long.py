#good pairs
'''for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    # print(l)
    r = -1
    count = 0
    sum = 0
    for i in range(len(l)):
        # print("l",l[i])
        if l[i] == r:
            count += 1
            # print("c",count)
            sum+=count
        else:
            count = 0
        r = l[i]
        # print("r",r)
    print(sum)'''


#CWIREFRAME
'''for _ in range(int(input())):
    a,b,x = map(int,input().split())
    sum = a+b
    print(2*x*sum)'''

#BOBBANK
'''for _ in range(int(input())):
    w,x,y,z = map(int,input().split())
    x = x-y
    print(w + x*z)'''

#SPEEDTEST
'''for _ in range(int(input())):
    a,b,x,y = map(int,input().split())
    if (a/b) > (x/y):
        print("Alice")
    elif (a/b) < (x/y):
        print("Bob")
    else:
        print("Equal")'''

#SUBARRY
#TEST CASES
'''1
7
5 7 3 2 -8 -1 -3'''
'''min
5 5
5 5
5 5
min
5 7
7 7
5 7
min
3 3
7 3
3 3
min
2 2
7 2
2 2
min
-8 -8
7 -8
2 -8
min
-8 -1
7 -1
1 -1
min
-8 -3
7 -3
1 -3
max
5 5
max
7 7
max
7 3
max
7 2
max
8 -8
max
8 -1
max
8 -3
-56 64'''
def calc_min(l):
    mn = l[0]
    mx=l[0]
    mb = abs(l[0])
    for i in range(len(l)):
        mn = min(mn,l[i])
        mx = max(mx,l[i])
        mb = min(mb,abs(l[i]))
    return min(mn*mx,mb*mb)

def calc_max(l):
    mb = abs(l[0])
    for i in range(len(l)):
        mb = max(mb,abs(l[i]))
    return mb*mb

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    print(calc_min(a),calc_max(a))
        
#PBATTLE
# 1. The function takes in a list of values.
# 2. It sorts the list and removes any duplicates.
# 3. It then assigns a value to each unique value in the list.
# 4. It then iterates through the list and replaces each value with its assigned value.
# 5. It then returns the list.
# from bisect import bisect_left, bisect_right


# def discrete(Q):
#     a = Q
#     a.sort()
#     a = list(set(a))
#     for i in range(len(Q)):
#         Q[i] = a.index(Q[i])
#     return Q


# for _ in range(int(input())):
#     n = int(input())
#     a = [int(x) for x in input().split()]
#     b = [int(x) for x in input().split()]
#     a = discrete(a)
#     b = discrete(b)
#     c = [0]*n
#     s = [0]*n
#     r = [0]*n
#     p = []
#     for i in range(n):
#         c[a[i]] = b[i]
#         s[i] = a[i]+b[i]
#         r[b[i]] = i
#     for i in range(n):
#         p.insert(bisect_right(0,len(p),p[i]),p[i])


# for i in range(n):
# p.insert(upper_bound(p,c[i]),c[i])
# s[r[c[i]]] = lower_bound(p,c[i])-p.begin()
# t = max(s)
# q = 0
# for i in s:
# if i == t:
# q += 1
# print(q)
# ```



# mod = 1000000007
# def power(b,n,mod):
#     s = 1
#     while(n):
#         if n%2 == 1: 
#             s = s*b%mod
#         b = b*b%mod
#         n/=2
#     return s

# def apower(a,b):
#     if b >=30:
#         return power(a,power(2,b,mod-1)+mod-1,mod)
#     return power(a,(1<<b),mod)


# def calc(n,p,k):
#     return (power(apower(n,k),p,mod)-power(n,p-1,mod)+mod)%mod*n%mod*power(n-1,mod-2,mod)%mod

# for _ in range(int(input())):
#     answer = 1
#     n,k = map(int,input().split())
#     for i in range(2,n+1):
#         s=0
#         while(n%i == 0):
#             s += 1
#             n /= i
#         if s!=0:
#             answer*=calc(i,s,k)%mod
#     if n!=1:
#         answer*=calc(n,1,k)%mod
#     print(answer)