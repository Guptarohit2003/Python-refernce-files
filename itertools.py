from itertools import product,permutations,combinations,combinations_with_replacement,groupby

# print(list(product([1,2,3],repeat=2)))

# print(list(product([1,2,3],[3,4])))

# A = [[1,2,3],[3,4,5]]
# print(list(product(*A)))

# B = [[1,2,3],[3,4,5],[7,8]]
# print(list(product(*B)))

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# l = list(product(a,b))
# print(*l)


# print(list(permutations([1,2,3])))

# print(list(permutations([1,2,3],2)))

# print(list(permutations('str')))


# s,k = map(str,input().split())
# s = sorted(s)
# k = int(k)
# x = list(permutations(s,k))
# for i in x:
#     print(''.join(i),sep="\n")

# print(list(combinations('12345',3)))
# A = [1,1,2,3,3,3]
# print(list(combinations(A,4)))

# s,k = map(str,input().split())
# s = sorted(s)
# k = int(k)
# for i in range(1,k+1):
#     for j in combinations(s,i):
#         print(''.join(j))

# print(list(combinations_with_replacement('12345',2)))    

# s,k = map(str,input().split())
# for i in combinations_with_replacement(sorted(s),int(k)):
#     print(''.join(i),sep="\n")

# for i,j in groupby(map(int,list(input()))):
#     print(tuple([len(list(j)),i]), end = " ")


# n = int(input())
# a = input().split()
# k = int(input())
# com = combinations(a,k)
# x = 0
# y = 0
# for i in com:
#     y += 1
#     if 'a' in i:
#         x+=1
# print(x)
# print(y)
# print(round((x/y),3))


k,m = map(int,input().split())
x = [[int(_) for _ in input().split()[1:]] for K in range(k)]
z = product(*x)
def fun(c):
    return sum([i**2 for i in c])%m

print(max([fun(j) for j in z]))

