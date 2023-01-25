from typing import Counter


for _ in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    X = Counter(A)
    val = list(X.values())
    val2 = set(val)
    count = 0
    if len(val2) == 1:
        print("YES")
    print(val)
    print(val2)