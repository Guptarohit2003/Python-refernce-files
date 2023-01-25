for _ in range(int(input())):
    s = input()
    f = 0
    if int(s[-1])%2 == 0:
        for i in range(len(s)-1):
            if int(s[i]) in [0,2,4,6,8]:
                f = 1
                break
    else:
        for i in range(len(s)-1):
            if int(s[i]) in [1,3,5,7,9]:
                f = 1
                break
    if  f== 0:
        print("NO")
    else:
        print("YES")