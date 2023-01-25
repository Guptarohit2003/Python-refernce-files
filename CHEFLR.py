for _ in range(int(input())):
    l = []
    s = str(input())
    mod = 10**9+7
    for i in range(len(s)):
        l.append(s[i])
    x = 1
    count = 1
    for i in range(len(l)):
        if l[i] == 'l':
            if count%2 != 0:
                x = 2*x
            else:
                x = 2*x-1
        elif l[i] == 'r': 
            if count%2 != 0:
                x = 2*x+2
            else:
                x = 2*x +1
        count+=1
        x = x%mod
    print(x)
