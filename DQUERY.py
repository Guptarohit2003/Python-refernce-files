def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
for _ in range(int(input())):
    n = int(input())
    m = list(map(int,input().split()))
    q = int(input())
    for i in range(q):
        p,k = input().split()
        p = int(p)
        k = int(k)
        s = 0
        sum = 0
        x = m[:]
        for i in range(len(m)):
            if m[i]%p == 0:
                s = i
                for j in range(s+1,len(m)):
                    # print(j,"j")
                    if m[j] > m[s] and m[j] %p == 0:
                        # print(m,j,s,"das")
                        swap(x,j,s)
        for l in range(0,k):
            sum += x[l]
        print(sum)

                