from collections import Counter
for _ in range(int(input())):
    N = int(input())
    a = list(map(int,input().split()))
    y = Counter(a)
    max_val = [val for val in y.values()]
    max_val.sort()
    f = max_val[-1]
    if f == N:
        print((f+1)//2)
        continue
    g = max_val[-2]
    print(max((f+1)//2,g))