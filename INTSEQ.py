def recur(k):
    if k%2 == 0:
        l.append(int(k/2))
        print(l)
        recur(int(k/2))
    if k == 1:
        return len(l)
    else:
        return len(l)


for _ in range(int(input())):
    k = int(input())
    l = []
    print(recur(k))